import csv

from src.models import Case


class CaseImporter:
    def __init__(self) -> None:
        pass

    def import_cases(self, filepath: str) -> list[Case]:
        with open(filepath) as f:
            reader = csv.DictReader(f, delimiter=';')
            cases = [Case.model_validate(row) for row in reader]
            return cases
