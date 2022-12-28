import pytest
from django.urls import reverse
from phantomas.errors import PhantomasRunError
from rest_framework.test import APIRequestFactory
from schema import Schema

from . import views

factory = APIRequestFactory()

expected_json = Schema({
    'message': str,
    'report': {
        'global_score': int,
        'data': dict
    }
})


def test_generate_report_view_with_post_method_success(patched_phantomas_wrapper):
    _, mocked_run = patched_phantomas_wrapper
    view = views.GenerateReport.as_view()

    request = factory.post(
        reverse('metrics_api:reports.generate'),
        {"page_url": "https://www.example.com/whatever"}
    )

    mocked_run.assert_not_called()
    response = view(request)
    mocked_run.assert_called_once()

    assert response.status_code == 200

    expected_json.validate(response.data)


def test_generate_report_view_with_post_method_validation_failed():
    """Test the validation of the request body param (`page_url`)."""

    view = views.GenerateReport.as_view()

    request = factory.post(
        reverse('metrics_api:reports.generate'),
        {"page_url": "not://a_valid.url/"}
    )

    response = view(request)

    assert response.status_code == 400

    Schema({
        'error': {
            'message': str
        }
    }).validate(response.data)


def raise_error():
    """Method used as a side_effect in the test method below."""
    raise PhantomasRunError("Connection timed out.")


@pytest.mark.parametrize(
    'patched_phantomas_wrapper',
    [{'side_effect': raise_error}],
    indirect=['patched_phantomas_wrapper']
)
def test_generate_report_view_with_post_method_error_on_page_fetching(
        patched_phantomas_wrapper
):
    """Test that the endpoint return an error when fetching the page fails."""
    _, mocked_run = patched_phantomas_wrapper
    view = views.GenerateReport.as_view()

    request = factory.post(
        reverse('metrics_api:reports.generate'),
        {"page_url": "https://a-valid-url.com/"}
    )

    mocked_run.assert_not_called()
    response = view(request)
    mocked_run.assert_called_once()

    assert response.status_code == 422
