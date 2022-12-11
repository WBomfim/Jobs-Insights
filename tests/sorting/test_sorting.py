import pytest
from src.pre_built.sorting import sort_by


@pytest.fixture()
def jobs_for_sort_by_criteria():
    return [
        {
            "id": 1,
            "max_salary": 1000,
            "min_salary": 500,
            "date_posted": "2020-01-01"
        },
        {
            "id": 2,
            "max_salary": 2000,
            "min_salary": 1000,
            "date_posted": "2020-01-02"
        },
        {
            "id": 3,
            "max_salary": 3000,
            "min_salary": 2000,
            "date_posted": "2020-01-03"
        },
        {
            "id": 4,
            "max_salary": 4000,
            "min_salary": 3000,
            "date_posted": "2020-01-04"
        },
    ]


def test_sort_by_criteria(jobs_for_sort_by_criteria):
    jobs = jobs_for_sort_by_criteria

    sort_by(jobs, "max_salary")
    for i in range(4):
        assert jobs[i]["id"] == 4 - i

    sort_by(jobs, "min_salary")
    for i in range(4):
        assert jobs[i]["id"] == i + 1

    sort_by(jobs, "date_posted")
    for i in range(4):
        assert jobs[i]["id"] == 4 - i

    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")

    with pytest.raises(TypeError):
        sort_by()
