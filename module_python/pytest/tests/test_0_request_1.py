import pytest

@pytest.fixture
def sample_data(request):

    x = request.param
    y = request.getfixturevalue
    z = request.fixturenames
    a = request.scope
    w = request.node
    return x, y, z, a, w


@pytest.mark.parametrize('sample_data', [1, "header", 3], indirect=True)
def test_sum(sample_data):
    print("передаём значения непоредственно в фисктуру через request.param и  indirect=True. Полученное значение = ", sample_data)



@pytest.fixture
def data(request):

    x = request.param
    y = request.getfixturevalue
    z = 33
    return x, y, z

@pytest.mark.parametrize("data", [("data111"), ("data222")], indirect=True)
def test_data(data):
    print(data)