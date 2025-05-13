from datetime import datetime, timedelta
import jdatetime

def get_next_day(date: datetime) -> datetime:
    return date + timedelta(days=1)

def get_next_month(date: datetime) -> datetime:
    month = date.month + 1 if date.month < 12 else 1
    year = date.year if date.month < 12 else date.year + 1
    return date.replace(year=year, month=month, day=1)

def get_next_year(date: datetime) -> datetime:
    return date.replace(year=date.year + 1, day=1, month=1)
    