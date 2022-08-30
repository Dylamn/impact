from unittest.mock import patch

import factory
from factory.faker import Faker

from accounts.tests.factories import UserFactory
from metrics.core import Runner
from metrics.models import Report
from metrics.tests.conftest import mocked_results


def get_metrics():
    url = 'https://www.example.com/factories'
    patcher = patch(
        'metrics.core.phantomas_wrapper.phantomas_wrapper.Phantomas.run',
        side_effect=mocked_results(url),
        autospec=True
    )
    patcher.start()

    _, results = Runner(url).start()

    patcher.stop()

    return results


class ReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Report

    uuid = Faker('uuid4')
    url = Faker('url')
    score = Faker('random_int', min=0, max=100, step=1)
    metrics = factory.LazyFunction(get_metrics)
    user = factory.SubFactory(UserFactory)
    previous_report = None
