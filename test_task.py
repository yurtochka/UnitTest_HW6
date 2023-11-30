import pytest

from task import TwoListsNum

list_1 = [15, 10, 1, 54, 4, 78]
list_2 = [88, 6, 98, 47, 1, 11]


def test_list_1():
    avg_lists = TwoListsNum(list_1, list_2)
    assert sorted(list_1) == sorted(avg_lists.list_1)


def test_list_2():
    avg_lists = TwoListsNum(list_1, list_2)
    assert sorted(list_2) == sorted(avg_lists.list_2)


def test_avg_list_1():
    avg_lists = TwoListsNum(list_1, list_2)
    assert avg_lists.average_first_list == 27


def test_avg_list_2():
    avg_lists = TwoListsNum(list_1, list_2)
    assert avg_lists.average_second_list == 41.8
