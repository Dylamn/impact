import pytest
from django.urls import reverse
from phantomas.errors import PhantomasRunError
from rest_framework.test import APIRequestFactory
from schema import Schema

from metrics_api import views
from .conftest import set_auth_header

factory = APIRequestFactory()

expected_json = Schema({
    'message': str,
    'report': {
        'global_score': int,
        'score_message': str,
        'data': dict
    }
})


@pytest.mark.current
def test_generate_report_view_with_post_method_success(
        db, patched_phantomas_wrapper, user_token
):
    _, mocked_run = patched_phantomas_wrapper
    view = views.GenerateReport.as_view()

    request = factory.post(
        reverse('metrics_api:reports.generate'),
        data={"page_url": "https://www.example.com/whatever"},
        **set_auth_header(user_token)
    )

    mocked_run.assert_not_called()
    response = view(request)
    mocked_run.assert_called_once()

    assert response.status_code == 200

    expected_json.validate(response.data)


def test_generate_report_view_with_post_method_validation_failed(db, user_token):
    """Test the validation of the request body param (`page_url`)."""

    view = views.GenerateReport.as_view()

    request = factory.post(
        reverse('metrics_api:reports.generate'),
        data={"page_url": "not://a_valid.url/"},
        **set_auth_header(user_token)
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
        db, patched_phantomas_wrapper, user_token
):
    """Test that the endpoint return an error when fetching the page fails."""
    _, mocked_run = patched_phantomas_wrapper
    view = views.GenerateReport.as_view()

    request = factory.post(
        reverse('metrics_api:reports.generate'),
        data={"page_url": "https://a-valid-url.com/"},
        **set_auth_header(user_token)
    )

    mocked_run.assert_not_called()
    response = view(request)
    mocked_run.assert_called_once()

    assert response.status_code == 422


def test_unauthorized_response_when_no_token_is_provided(patched_phantomas_wrapper):
    """Test that the endpoint return an Unauthorized response (401).

    The endpoint should return a 401 when no `Authorization` header is provided with
    a valid token.
    """
    _, mocked_run = patched_phantomas_wrapper
    view = views.GenerateReport.as_view()

    request = factory.post(
        reverse('metrics_api:reports.generate'),
        data={"page_url": "https://a-valid-url.com/"},
    )

    mocked_run.assert_not_called()
    response = view(request)
    mocked_run.assert_not_called()

    assert response.status_code == 401
