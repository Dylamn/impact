from unittest import mock

import pytest
from schema import Schema

from metrics.core.phantomas_wrapper import PhantomasWrapper
from metrics.tests.conftest import mocked_results


@pytest.fixture
def patched_phantomas_wrapper() -> (PhantomasWrapper, mock.MagicMock):
    patcher = mock.patch(
        'metrics.core.phantomas_wrapper.phantomas_wrapper.Phantomas.run',
        side_effect=mocked_results('https://www.example.com/phantomas/test')
    )
    mocked_run = patcher.start()
    url = 'https://www.example.com/phantomas/test'

    yield PhantomasWrapper(url), mocked_run

    patcher.stop()


results_schema = Schema({
    'dom': {
        'label': str,
        'metrics': {
            'dom_length': int,
            'dom_max_depth': int,
            'dom_id_duplicated': int,
            'iframes_count': int,
        }
    },
    'javascript': {
        'label': str,
        'metrics': {
            'accesses_count': int,
            'js_exec_duration': int,
            'synchronous_ajax': int,
        }
    },
    'css': {
        'label': str,
        'metrics': {
            'inline_css': int,
        }
    },
    'requests': {
        'label': str,
        'metrics': {
            'requests': int,
            'domains': int,
            'not_found': int,
            'below_the_fold_images': int,
        }
    },
    'server_config': {
        'label': str,
        'metrics': {
            'old_http_protocol': int,
            'old_tls_protocol': int,
            'caching_disabled': int,
            'caching_not_specified': int,
        }
    }
})


def test_phantomas_wrapper_call_all_metrics_modules(
        patched_phantomas_wrapper
) -> None:
    """Tests that all metrics modules are called."""
    phantomas_wrapper, mocked_run = patched_phantomas_wrapper
    patchers = []
    for module in phantomas_wrapper.modules:
        patcher = mock.patch.object(module, 'get_metrics')
        patcher.start()
        patchers.append(patcher)

    mocked_run.assert_not_called()
    phantomas_wrapper.run()
    mocked_run.assert_called_once()

    for patcher in patchers:
        mocked_method, _ = patcher.get_original()
        mocked_method.assert_called_once()
        patcher.stop()


def test_phantomas_wrapper_results(
        patched_phantomas_wrapper
) -> None:
    phantomas_wrapper, mocked_run = patched_phantomas_wrapper
    results = phantomas_wrapper.run()

    mocked_run.assert_called_once()

    results_schema.validate(results)
