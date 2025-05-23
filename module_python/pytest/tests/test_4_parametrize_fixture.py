import random
import pytest

"""auto = ("BMW", "E39", 2.0), ("AUDI", "A6", 2.4), ("FORD", "MONDEO", 2.0), ("MAZDA", "6", 1.8)

@pytest.fixture
def car():
    return auto[random.randrange(0,4)]

def test_driver_choise(car):
    assert car == auto[random.randrange(0,4)]

"""

# ПАРАМЕТРИЗАЦИЯ ФИКСТРУРЫ

auto = ("BMW", "E39", 2.0), ("AUDI", "A6", 2.4), ("FORD", "MONDEO", 2.0), ("MAZDA", "6", 1.8)

# Параметризуем фикстуру car
@pytest.fixture(params=auto, ids=["t1", "t2","t3","t4"])
def car(request):
    print(request.param)
    return request.param

def test_driver_choice(car):
    assert car in auto
