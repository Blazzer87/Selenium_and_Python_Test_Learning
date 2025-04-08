import pytest

@pytest.fixture(autouse=True, scope="function", params=["chromium", "firefox"])
def fixture(request):
    return request.param  # Используйте request.param вместо request.params

def test(fixture):
    print(type(fixture))
    print(fixture)



