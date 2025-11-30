import csv

from src.models import Case

def import_cases(filepath: str) -> list[Case]:
    with open(filepath) as f:
        reader = csv.DictReader(f)
        cases = [Case.model_validate(row) for row in reader]
        return cases
