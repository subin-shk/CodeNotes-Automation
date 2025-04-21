import pytest


@pytest.fixture
def valid_credentials():
    return {
        "email": "example@example.com",
        "password": "Password123",
        "confirm_password": "Password123",
    }


@pytest.fixture
def invalid_credentials():
    return {
        "email": "",
        "password": "Password123",
        "confirm_password": "aadsassword123",
    }
