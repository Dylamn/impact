import pytest

from accounts.tests.factories import UserFactory


@pytest.fixture()
@pytest.mark.django_db
def user_token():
    user = UserFactory.create()

    return user.auth_token.key


def set_auth_header(token, prefix='Token'):
    return {'HTTP_AUTHORIZATION': f'{prefix} {token}'}
