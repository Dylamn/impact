from schema import Schema

from metrics.core import Runner
from metrics.tests.conftest import mocked_results


def test_runner_results(mocker, phantomas_results):
    """Test the results that the runner returns."""
    category_dict = {
        'label': str, 'metrics': dict, 'weight': int, 'rules': dict, 'score': int,
        'note': str,
    }
    expected_schema = Schema({
        'dom': category_dict,
        'server_config': category_dict,
        'css': category_dict,
        'javascript': category_dict,
        'requests': category_dict
    })
    url = 'https://www.example.com/runner_test'

    mocker.patch(
        'metrics.core.phantomas_wrapper.phantomas_wrapper.Phantomas.run',
        side_effect=mocked_results(url)
    )
    runner = Runner(url)

    assert runner.url == url

    score, results = runner.start()

    assert isinstance(score, int)
    expected_schema.validate(results)
