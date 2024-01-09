import pytest
from ...aocutils import Grid


@pytest.fixture
def sample_grid():
    # Fixture to create a sample grid for testing
    return Grid([[1, 2], [3, 4]], sep=", ")


def test_initialization():
    grid = Grid()
    assert grid.content == []
    assert grid.sep == ""

    content = [[1, 2], [3, 4]]
    sep = ", "
    grid = Grid(content, sep)
    assert grid.content == content
    assert grid.sep == sep


def test_append_row():
    grid = Grid([[1, 2], [3, 4]], sep=", ")
    grid.append_row([5, 6])
    assert grid.content == [[1, 2], [3, 4], [5, 6]]


def test_pad():
    grid = Grid([[1, 2], [3, 4]], sep=", ")
    grid.pad()
    assert str(grid) == "., ., ., .\n., 1, 2, .\n., 3, 4, .\n., ., ., ."


def test_str():
    grid = Grid([[1, 2], [3, 4]], sep=", ")
    assert str(grid) == "1, 2\n3, 4"


def test_getitem():
    grid = Grid([[1, 2], [3, 4]], sep=", ")
    assert grid[0, 0] == 1
    assert grid[1, 1] == 4


def test_setitem():
    grid = Grid([[1, 2], [3, 4]], sep=", ")
    grid[0, 0] = 0
    assert grid.content == [[0, 2], [3, 4]]


def test_shape():
    grid = Grid([[1, 2, 3], [4, 5, 6]], sep=", ")
    assert grid.shape == (2, 3)


def test_get_subset():
    grid = Grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], sep=", ")
    subset = grid.get_subset(0, 1, 1, 2)
    assert subset.content == [[2, 3], [5, 6]]
