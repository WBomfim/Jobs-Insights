import pytest
from src.pre_built.brazilian_jobs import read_brazilian_file

PATH = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    jobs = read_brazilian_file(PATH)
    for job in jobs:
        assert "titulo" not in job
        assert "salario" not in job
        assert "tipo" not in job

        assert "title" in job
        assert "salary" in job
        assert "type" in job

    with pytest.raises(FileNotFoundError):
        read_brazilian_file("jobs_not_found.csv")
