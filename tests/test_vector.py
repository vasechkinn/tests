import pytest
from vector import Vector

@pytest.fixture
def vector_1():
    return Vector(1, 2, 3)

@pytest.fixture
def vector_2():
    
    return Vector(1, 2, 3)

@pytest.fixture
def vector_coll():
    
    return Vector(2, 4, 6)

@pytest.fixture
def vector_anti_coll():
    
    return Vector(-2, -4, -6)

@pytest.fixture
def vector_ortogonal():
    
    return Vector(-2, 1, 0)

@pytest.fixture
def vector_zero_len():
    
    return Vector(0, 0, 0)

def test_add(vector_1, vector_2):
    res = vector_1.add(vector_2)

    assert res.get_x() == 2, f" exp: {2}, res: {res.get_x}"
    assert res.get_y() == 4, f" exp: {4}, res: {res.get_y}"
    assert res.get_z() == 6, f" exp: {6}, res: {res.get_z}"

def test_sub(vector_1, vector_2):
    res = vector_1.sub(vector_2)

    assert res.get_x() == 0, f" exp: {0}, res: {res.get_x}"
    assert res.get_y() == 0, f" exp: {0}, res: {res.get_y}"
    assert res.get_z() == 0, f" exp: {0}, res: {res.get_z}"

def test_len(vector_1):
    expected = 3.74
    res = vector_1.length()

    assert res == expected, f"res: {res}, expected: {expected}"

def test_colliniar_vector(vector_1, vector_coll):
    expected = 0
    res = vector_1.angle_between(vector_coll)

    assert res == expected, f"res: {res}, expected: {expected}"

def test_anti_colliniar_vector(vector_1, vector_anti_coll):
    expected = 3.14
    res = vector_1.angle_between(vector_anti_coll)

    assert res == expected, f"res: {res}, expected: {expected}"

def test_ortogonal_vector(vector_1, vector_ortogonal):
    expected = 1.57
    res = vector_1.angle_between(vector_ortogonal)

    assert res == expected, f"res: {res}, expected: {expected}"

def test_rand(vector_1):
    res = vector_1.random()

    assert -100 <= res.get_x() <= 100, f"res: {res.get_x}"
    assert -100 <= res.get_y() <= 100, f"res: {res.get_y}"
    assert -100 <= res.get_z() <= 100, f"res: {res.get_z}"

def test_ne_tot_tip():
    with pytest.raises(TypeError):
        Vector(1, '2', 3)

def test_zero_div(vector_1, vector_zero_len):
    with pytest.raises(ZeroDivisionError):
        vector_1.angle_between(vector_zero_len)

def test_rand_count(vector_1):
    res = vector_1.random()
    assert isinstance(res, Vector)