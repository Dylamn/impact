import json
import pathlib

import pytest


class PhantomasResultsMock:
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
