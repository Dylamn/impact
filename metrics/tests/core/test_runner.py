import pytest

from metrics.core import Runner


def test_runner_initialization():
    url = 'https://www.example.com'

    runner = Runner(url)

@pytest.skip("Need implementation")
def test_runner_results():
    runner = Runner('https://www.example.com')

    assert runner.start() == {'success': True}

