import pytest
from developer.models import Developer
from django.contrib.auth.hashers import pbkdf2, make_password


@pytest.fixture(scope='module')
def new_developer():
    hased_password = make_password('password123')
    params = {
        'firstname': 'test_dev1',
        'lastname': 'test_dev1',
        'email': 'test_dev1@test.com',
        'date_of_birth': '1992-01-01',
        'mobile': '08027538232',
        # 'password': 'pbkdf2_sha256$150000$ah3ccoAH5eS5$fv/61uyxCYq6Pv5GGVB6gQs0s7NBw8tcbzHSLZoFr78=',
        'password': hased_password,
        'is_active': True,
        'is_admin': False,
    }
    developer = Developer(**params)
    return developer
