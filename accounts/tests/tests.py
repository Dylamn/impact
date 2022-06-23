import pytest
from django.test import TestCase
from accounts.models import User


# Create your tests here.
def test_assert_true_is_true():
    assert True


@pytest.mark.django_db
def test_user_create():
    """Test user creation."""
    assert User.objects.count() == 0
    User.objects.create_user('John', 'lennon@example.com', 'password123')
    assert User.objects.count() == 1
