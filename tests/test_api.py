import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_date_info_gregorian():
    response = client.get("/date-info", params={"date": "2024-09-01", "calendar": "gregorian"})
    assert response.status_code == 200
    data = response.json()
    assert data["input_date_gregorian"] == "2024-09-01"
    assert data["input_date_jalali"] == "1403-06-11"
    assert "YYYY-MM-DD" in data["format_variants"]
    assert isinstance(data["all_days_gregorian"], list)
    assert isinstance(data["weekends"], list)

def test_get_date_info_jalali():
    response = client.get("/date-info", params={"date": "1403-06-11", "calendar": "jalali"})
    assert response.status_code == 200
    data = response.json()
    assert data["input_date_gregorian"] == "2024-09-01"
    assert data["input_date_jalali"] == "1403-06-11"