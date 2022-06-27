from django.utils.crypto import get_random_string


def create_user_data(i: int = 0) -> dict:
    """Generate simple user data for filling the signup form."""
    random_password = get_random_string(16)

    return {
        "username": f"user{i}",
        "email": f"user{i}@example.com",
        "first_name": f"firstname{i}",
        "last_name": f"lastname{i}",
        "password": random_password,
        "confirm_password": random_password,
    }
