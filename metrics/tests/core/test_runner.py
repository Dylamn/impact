import pytest

from metrics.core import Runner


def test_runner_initialization():
    url = 'https://www.example.com'

    runner = Runner(url)


def test_runner_results():
    pytest.skip("Need implementation")
    runner = Runner('https://www.example.com')

    assert runner.start() == {'success': True}

