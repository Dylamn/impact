import json
import pathlib
from unittest import mock

import pytest

from metrics.core.phantomas_wrapper import PhantomasWrapper


class PhantomasResultsMock(object):
    def __init__(self, url, data):
        for key in ['generator', 'metrics', 'offenders']:
            assert data.get(key) is not None

        self._url = url

        self._generator = data.get('generator')
        self._metrics = data.get('metrics')
        self._offenders = data.get('offenders')

    def get_metric(self, name, default=None):
        """ Get metric value """
        return self._metrics.get(name, default)

    def get_metrics(self):
        """ Get all metrics as key/value dict """
        return self._metrics

    def get_offenders(self, name):
        """ Get offenders for a given metric """
        return self._offenders.get(name)

    def get_url(self):
        """ Get URL of the pages phantomas has been run for """
        return self._url


@pytest.fixture()
def phantomas_results():
    path_to_tests = pathlib.Path(__file__).parent

    with open(path_to_tests / 'samples/phantomas.json', 'r') as json_file:
        parsed_json = json.load(json_file)
        yield PhantomasResultsMock(url='https://www.example.com', data=parsed_json)


def mocked_results(url):
    """Return a phantomas `run` results"""
    from django.conf import settings

    with open(settings.BASE_DIR / 'metrics/tests/samples/phantomas.json') as f:
        yield PhantomasResultsMock(url, json.load(f))


@pytest.fixture()
def patched_phantomas_wrapper(request) -> (PhantomasWrapper, mock.MagicMock):
    """Fixture that patch the `run` method of the PhantomasWrapper class."""
    url = 'https://www.example.com/phantomas/test'

    if hasattr(request, 'param') and isinstance(request.param, dict):
        url = request.param.get('url', url),
        side_effect = request.param.get('side_effect')
    else:
        side_effect = mocked_results(url)

    patcher = mock.patch(
        'metrics.core.phantomas_wrapper.phantomas_wrapper.Phantomas.run',
        side_effect=side_effect
    )
    mocked_run = patcher.start()

    yield PhantomasWrapper(url), mocked_run

    patcher.stop()
