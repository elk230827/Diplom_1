from praktikum.database import Database
import pytest

@pytest.fixture
def db():
    return Database()