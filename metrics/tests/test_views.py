import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains

from accounts.tests.factories import UserFactory
from metrics.models import Report
from metrics.tests.conftest import mocked_results
from metrics.tests.factories import ReportFactory
from metrics.core.rules import phantomas_rules


@pytest.mark.django_db
def test_run_view(client, mocker, phantomas_results):
    """Test that the view create a new report and redirect to another view."""
    test_url = 'https://www.example.com/test1'

    mock = mocker.patch(
        'metrics.core.phantomas_wrapper.phantomas_wrapper.Phantomas.run',
        side_effect=mocked_results(test_url), autospec=True
    )

    assert Report.objects.filter(url=test_url).exists() is False
    mock.assert_not_called()

    response = client.post(reverse('metrics:run'), data={
        "page_url": test_url
    })

    mock.assert_called_once()
    assert response.status_code == 301
    assert '/metrics/results' in response.url

    assert Report.objects.filter(url=test_url).exists()


@pytest.mark.django_db
def test_report_view(client):
    report = ReportFactory()

    response = client.get(reverse('metrics:results', args=(report.uuid,)))

    assert response.status_code == 200
    assertTemplateUsed(response, 'metrics/results.html')
    assertTemplateUsed(response, 'metrics/cta.html')
    assertTemplateUsed(response, 'metrics/report/report.html')


@pytest.mark.django_db
def test_report_specific_metric_view(client):
    report = ReportFactory()

    category = 'css'
    metric = 'inline_css'

    url = reverse('metrics:results', args=(report.uuid, category, metric))

    response = client.get(url)

    assert response.status_code == 200
    assertTemplateUsed(response, 'metrics/metric.html')
    assertContains(response, phantomas_rules.get(metric)['message'])


@pytest.mark.django_db
def test_compare_reports_require_login(client):
    first_report = ReportFactory()
    second_report = ReportFactory()
    url = reverse('metrics:compare', args=(second_report.uuid, first_report.uuid))

    response = client.get(url)

    assert response.status_code == 302
    assert response.url == f'/login/?next={url}'


@pytest.mark.django_db
def test_compare_reports_view_success(client):
    user = UserFactory()
    first_report = ReportFactory(user=user)
    second_report = ReportFactory(
        url=first_report.url, user=user, previous_report=first_report
    )

    url = reverse('metrics:compare', args=(second_report.uuid, first_report.uuid))

    client.force_login(user)
    response = client.get(url)

    assert response.status_code == 200
    assertTemplateUsed(response, 'metrics/report/report.html')
    assertTemplateUsed(response, 'metrics/compare.html')


@pytest.mark.django_db
def test_compare_reports_with_different_url_failure(client):
    user = UserFactory()
    first_report = ReportFactory(user=user)
    second_report = ReportFactory(user=user)
    url = reverse('metrics:compare', args=(second_report.uuid, first_report.uuid))

    client.force_login(user)
    response = client.get(url)

    assert response.status_code == 400


@pytest.mark.django_db
def test_compare_reports_of_another_user_failure(client):
    user = UserFactory()
    first_report = ReportFactory(user=user)
    second_report = ReportFactory()
    url = reverse('metrics:compare', args=(second_report.uuid, first_report.uuid))

    client.force_login(user)
    response = client.get(url)

    assert response.status_code == 403
