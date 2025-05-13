from datetime import datetime
import jdatetime
from utils.calendar_info import (
    get_all_days_of_month,
    get_all_days_of_jalali_month,
    get_weekends,
    get_month_name_gregorian,
    get_month_name_jalali
)

def test_get_all_days_of_month():
    date = datetime(2024, 9, 1)
    days = get_all_days_of_month(date)
    assert len(days) == 30
    assert days[0] == '2024-09-01'

def test_get_all_days_of_jalali_month():
    j_date = jdatetime.date(1403, 6, 1)
    days = get_all_days_of_jalali_month(j_date)
    assert '1403-06-01' in days
    assert len(days) in (30, 31)  # Shamsi months can be 30 or 31 days

def test_get_weekends():
    date = datetime(2024, 9, 1)
    weekends = get_weekends(date)
    for day in weekends:
        weekday = datetime.strptime(day, "%Y-%m-%d").weekday()
        assert weekday in [4, 5]  # Friday, Saturday

def test_month_names():
    date = datetime(2024, 9, 1)
    assert get_month_name_gregorian(date) == 'September'
    assert get_month_name_jalali(date) == 'شهریور'
