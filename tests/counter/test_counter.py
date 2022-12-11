import pytest
from src.pre_built.counter import count_ocurrences

PATH = "tests/mocks/jobs.csv"
COUNT_DEVELOPER_WORD = 3


def test_counter():
    assert count_ocurrences(PATH, "developer") == COUNT_DEVELOPER_WORD
    assert count_ocurrences(PATH, "DEVELOPER") == COUNT_DEVELOPER_WORD

    with pytest.raises(TypeError):
        count_ocurrences(PATH)
        count_ocurrences("developer")

    with pytest.raises(FileNotFoundError):
        count_ocurrences("jobs_not_found.csv", "developer")
