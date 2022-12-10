from typing import Union, Dict


def validate_job_salaries_info(job: Dict) -> None:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary and max_salary must be in job")

    min_salary, max_salary = job["min_salary"], job["max_salary"]

    if (
        not type(max_salary) == int or not str(max_salary).isnumeric()
    ):
        raise ValueError("max_salary must be numeric")

    if (
        not type(min_salary) == int or not str(min_salary).isnumeric()
    ):
        raise ValueError("min_salary must be numeric")

    if int(min_salary) > int(max_salary):
        raise ValueError("min_salary must be less than max_salary")


def validate_salary(salary: Union[int, str]) -> None:
    if not type(salary) == int and not type(salary) == str:
        raise ValueError("salary must be an int or a numeric str")

    if type(salary) == str and not salary.isnumeric():
        raise ValueError("salary must be numeric")
