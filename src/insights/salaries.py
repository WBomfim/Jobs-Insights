from typing import Union, List, Dict
from src.insights.jobs import read
from src.insights.validate_infos import (
    validate_job_salaries_info,
    validate_salary
)


def get_max_salary(path: str) -> int:
    return max(int(job["max_salary"])
               for job in read(path) if job["max_salary"].isnumeric())


def get_min_salary(path: str) -> int:
    return min(int(job["min_salary"])
               for job in read(path) if job["min_salary"].isnumeric())


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validate_job_salaries_info(job)
    validate_salary(salary)
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
