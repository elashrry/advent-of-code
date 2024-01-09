import pytest

from utils import IntInterval, Subset


@pytest.fixture
def interval():
    return IntInterval(1, 5, closed="left")


def test_init():
    interval = IntInterval(1, 5, closed="left")
    assert interval.start == 1
    assert interval.end == 4
    assert interval.width == 3
    assert interval.num_elems == 4

    interval = IntInterval(1, 5, closed="right")
    assert interval.start == 2
    assert interval.end == 5
    assert interval.width == 3

    interval = IntInterval(1, 5, closed=True)
    assert interval.start == 1
    assert interval.end == 5
    assert interval.width == 4

    interval = IntInterval(1, 5, closed=False)
    assert interval.start == 2
    assert interval.end == 4
    assert interval.width == 2


def test_contains(interval):
    assert all([interval.contains(i) for i in range(1, 5)])
    assert not interval.contains(5)
    assert not interval.contains(6)


def test_intersection(interval):
    other1 = IntInterval(3, 7, closed="left")
    other2 = IntInterval(-3, 2, closed="right")
    other3 = IntInterval(4, 5, closed="left")
    other4 = IntInterval(6, 10, closed="left")
    assert interval.intersection(other1) == IntInterval(3, 4, closed=True)
    assert interval.intersection(other2) == IntInterval(1, 2, closed=True)
    assert interval.intersection(other3) == IntInterval(4, 4, closed=True)
    assert interval.intersection(other4) is None


def test_unions(interval):
    other1 = IntInterval(3, 7, closed="left")
    other2 = IntInterval(-6, 10, closed="right")
    other3 = IntInterval(8, 12, closed="right")
    assert interval.union(other1) == IntInterval(1, 6, closed=True)
    assert interval.union(other2) == other2
    assert interval.union(other3).content == [interval, other3]


def test_difference(interval):
    other1 = IntInterval(3, 7, closed="left")
    other2 = IntInterval(4, 6, closed="right")
    other3 = IntInterval(6, 10, closed="left")
    assert interval.difference(other1) == IntInterval(1, 2, closed=True)
    assert interval.difference(other2) == IntInterval(1, 4, closed=True)
    assert interval.difference(other3) == interval


def test_repr(interval):
    assert repr(interval) == "[1, 4]"


def test_eq():
    interval1 = IntInterval(1, 5, closed="left")
    interval2 = IntInterval(1, 5, closed="left")
    interval3 = IntInterval(1, 5, closed="right")
    interval4 = IntInterval(1, 4, closed=True)
    assert interval1 == interval2
    assert interval1 == interval4
    assert interval1 != interval3


def test_clean_intervals():
    interval1 = IntInterval(1, 5, closed="left")
    interval2 = IntInterval(3, 7, closed="left")
    interval3 = IntInterval(6, 8, closed=True)
    interval4 = IntInterval(8, 10, closed="right")
    interval5 = IntInterval(12, 15, closed=False)
    interval6 = IntInterval(1, 15)

    # case 1: empty list
    cleaned_empty_subset = Subset([])._clean_intervals([])
    assert len(cleaned_empty_subset) == 0

    # case 2: one single interval
    cleaned_single_interval_subset = Subset([])._clean_intervals([interval1])
    assert len(cleaned_single_interval_subset) == 1
    assert cleaned_single_interval_subset[0] == interval1

    # case 3: different intersection, tangent
    interval_list = [interval1, interval2, interval3, interval4, interval5]
    cleaned_subset = Subset([])._clean_intervals(interval_list)
    assert len(cleaned_subset) == 3
    assert cleaned_subset[0].start == 1
    assert cleaned_subset[0].end == 8
    assert cleaned_subset[1].start == 9
    assert cleaned_subset[1].end == 10
    assert cleaned_subset[2].start == 13
    assert cleaned_subset[2].end == 14

    # case 4: one interval contain everything
    interval_list.append(interval6)
    cleaned_subset = Subset([])._clean_intervals(interval_list)
    assert len(cleaned_subset) == 1
    assert cleaned_subset[0].start == 1
    assert cleaned_subset[0].end == 14
