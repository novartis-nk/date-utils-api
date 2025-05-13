from datetime import datetime
from utils.converters import gregorian_to_jalali, jalali_to_gregorian

def test_gregorian_to_jalali():
    g_date = datetime(2024, 9, 1)
    j_date = gregorian_to_jalali(g_date)
    assert j_date == '1403-06-11'

def test_jalali_to_gregorian():
    j_date = '1403-06-11'
    g_date = jalali_to_gregorian(j_date)
    assert g_date.strftime('%Y-%m-%d') == '2024-09-01'
