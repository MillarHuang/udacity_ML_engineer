# conftest.py
import pytest

@pytest.fixture(scope="module", params=[2,5])
def variables(request):
    value = request.param
    return value
# Creating a Dataframe object 'pytest.df' in Namespace
def pytest_configure():
    pytest.value = 6