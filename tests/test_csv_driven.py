import csv
import os
import pytest
from slugify import slugify

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "test_data.csv")


def load_data():
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        return [(r["text"], r["algorithm"], r["expected"]) for r in csv.DictReader(f)]


@pytest.mark.data_driven
@pytest.mark.parametrize("text,algo,expected", load_data())
def test_slugify_from_csv(text, algo, expected):
    assert slugify(text, algorithm=algo) == expected