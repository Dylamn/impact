import pytest
from django.db.models import ObjectDoesNotExist
from django.shortcuts import reverse
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from accounts.models import User
from .factories import UserFactory
from .helpers import create_user_data


@pytest.mark.current
@pytest.mark.django_db
def test_create_user_generates_token():
    """Test that a token is generated for a newly created user (post_save signal)."""
    new_user = UserFactory.build()

    with pytest.raises(ObjectDoesNotExist):
        token = new_user.auth_token

    new_user.save()

    token = new_user.auth_token

    assert token is not None and isinstance(token.key, str)


@pytest.mark.selenium
@pytest.mark.usefixtures('use_driver')
class SeleniumTests:
    def test_signup(self, live_server):
        """Test the register page form with selenium."""
        user_data = create_user_data(7)
        url = live_server.url + reverse('signup')

        self.driver.get(url)

        assert self.driver.title == 'Impact — Signup'

        # Get the form elements
        username_field = self.driver.find_element(By.ID, 'username')
        email_field = self.driver.find_element(By.ID, 'email')
        firstname_field = self.driver.find_element(By.ID, 'first_name')
        lastname_field = self.driver.find_element(By.ID, 'last_name')
        password_field = self.driver.find_element(By.ID, 'password')
        cfrm_password_field = self.driver.find_element(By.ID, 'confirm_password')
        signup_button = self.driver.find_element(By.ID, 'signup')

        # Fill the fields with value
        username_field.send_keys(user_data['username'])
        email_field.send_keys(user_data['email'])
        firstname_field.send_keys(user_data['first_name'])
        lastname_field.send_keys(user_data['last_name'])
        password_field.send_keys(user_data['password'])
        cfrm_password_field.send_keys(user_data['confirm_password'])

        signup_button.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_changes(url)
        )

        # Check if the user has been created
        assert User.objects.filter(email=user_data['email']).exists()

    def test_login_success(self, live_server):
        email = 'gally@example.com'
        password = 'Password123-=+'
        User.objects.create_user('Gally', email, password)

        url = live_server.url + reverse('login')

        self.driver.get(url)

        email_field = self.driver.find_element(By.ID, 'email')
        password_field = self.driver.find_element(By.ID, 'password')
        submit_button = self.driver.find_element(By.ID, 'login_button')

        email_field.send_keys(email)
        password_field.send_keys(password)

        submit_button.send_keys(Keys.ENTER)
        # The cookie named ``sessionid`` means a user is authenticated.
        sessionid_cookie = self.driver.get_cookie('sessionid')

        assert sessionid_cookie is not None
        assert sessionid_cookie.get('value')
