from datetime import datetime
from utils.next_dates import get_next_day, get_next_month, get_next_year

def test_get_next_day():
    date = datetime(2024, 9, 1)
    assert get_next_day(date).strftime('%Y-%m-%d') == '2024-09-02'

def test_get_next_month():
    date = datetime(2024, 9, 1)
    assert get_next_month(date).strftime('%Y-%m-%d') == '2024-10-01'

def test_get_next_year():
    date = datetime(2024, 9, 1)
    assert get_next_year(date).strftime('%Y-%m-%d') == '2025-01-01'
