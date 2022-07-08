import pytest


class PhantomasMock:
    def __init__(self, url, **kwargs):
        self._url = url

    def run(self):
        with open('phantomas.json') as f:
            ...


def test_phantomas_wrapper_results(mocker):
    assert True
    # mocker.patch(
    #     'metrics.core.phantomas_wrapper.phantomas.Phantomas.run',
    #
    # )
