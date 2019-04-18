import pytest
from developer.models import Developer


@pytest.fixture(scope='module')
def new_developer():
    params = {
        'firstname': 'test_dev1',
        'lastname': 'test_dev1',
        'email': 'test_dev1@test.com',
        'date_of_birth': '1992-01-01',
        'mobile': '08027538232'
    }
    developer = Developer(**params)
    return developer
