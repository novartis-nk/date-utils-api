import calendar
import jdatetime
from datetime import datetime

def get_all_days_of_month(date: datetime) -> list:
    year, month = date.year, date.month
    return [datetime(year, month, day).strftime('%Y-%m-%d') for day in range(1, calendar.monthrange(year, month)[1] + 1)]

def get_all_days_of_jalali_month(j_date: jdatetime.date) -> list:
    return [j_date.replace(day=1).replace(day=day).strftime('%Y-%m-%d')
            for day in range(1, jdatetime.j_days_in_month[j_date.month - 1] + 1)]

def get_weekends(date: datetime) -> list:
    year, month = date.year, date.month
    return [datetime(year, month, day).strftime('%Y-%m-%d')
            for day in range(1, calendar.monthrange(year, month)[1] + 1)
            if datetime(year, month, day).weekday() in [4, 5]]  # Friday, Saturday

def get_month_name_gregorian(date: datetime) -> str:
    return date.strftime('%B')

def get_month_name_jalali(date: datetime) -> str:
    # Mapping Latin month names to Persian
    latin_to_persian_months = {
        "Farvardin": "فروردین",
        "Ordibehesht": "اردیبهشت",
        "Khordad": "خرداد",
        "Tir": "تیر",
        "Mordad": "مرداد",
        "Shahrivar": "شهریور",
        "Mehr": "مهر",
        "Aban": "آبان",
        "Azar": "آذر",
        "Dey": "دی",
        "Bahman": "بهمن",
        "Esfand": "اسفند"
    }

    # Convert Gregorian to Jalali
    jdate = jdatetime.date.fromgregorian(date=date)
    
    # Get the Latin month name
    latin_month_name = jdate.strftime('%B')
    
    # Return the corresponding Persian month name
    return latin_to_persian_months.get(latin_month_name, latin_month_name)