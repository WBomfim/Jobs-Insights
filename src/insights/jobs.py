from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        return [row for row in csv.DictReader(file)]


def get_unique_job_types(path: str) -> List[str]:
    return {jobs["job_type"] for jobs in read(path)}


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
