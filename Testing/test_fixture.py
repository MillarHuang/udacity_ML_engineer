# import pytest
# @pytest.fixture(scope="module", params=[2,5])
# def resource(request):
#     print("Setting up the resource for the module")
#     value = request.param
#     return value

# @pytest.fixture(scope="module", params=[3])
# def resource_2(request):
#     print("Setting up the resource for the module")
#     value = request.param
#     return value

# def test_one(resource,resource_2):
#     assert (resource <=10) & (resource_2 <=5)

# def test_two(resource,resource_2):
#     assert (resource >= 0) & (resource_2 >=0)

#Use global variable specified in pytest namespace
import pytest
# Test function
# See the `pytest.df = df` statement to store the variable in Namespace
def test_import_data():
    df = pytest.value
    assert df == 6
    pytest.value = df +1
    # return df
# Test function
# See the `df = pytest.df` statement accessing the Dataframe object from Namespace
def test_function_two():
    df = pytest.value
    assert df == 7

def test_variables(variables):
    assert (variables >= 0) & (variables <= 10)


# Store test cases result in cache
# It uses the built-in request fixture
def test_cache_one(request):
    df = 5
    request.config.cache.set('cache_v', df)
    assert df == 5


# Test function
def test_cache_two(request):
    df = request.config.cache.get('cache_v', None)
    assert df == 5


