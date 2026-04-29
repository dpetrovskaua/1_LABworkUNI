import pytest
from main import Matrix

@pytest.fixture
def matrix():
    return Matrix()

def test_initialization(matrix):
    assert matrix.length == 0
    assert matrix.A == []
    
def test_multiply_logic(matrix):
    matrix.length = 2
    matrix.A = [[1, 1],
                [1, 1]]
    matrix.B = [[2, 2],
                [2, 2]]
    matrix.multiply()
    assert matrix.C == [[4, 4],
                        [4, 4]]

def test_average_calculation(matrix):
    matrix.C = [[10, 20],
                [30, 40]]
    # (10+20+30+40) / 4 = 25
    assert matrix.get_average() == 25.0
