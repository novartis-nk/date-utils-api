import jdatetime
from datetime import datetime

def gregorian_to_jalali(g_date: datetime) -> str:
    return jdatetime.date.fromgregorian(date=g_date).strftime('%Y-%m-%d')

def jalali_to_gregorian(j_date: str) -> datetime:
    y, m, d = map(int, j_date.split('-'))
    return jdatetime.date(year=y, month=m, day=d).togregorian()
