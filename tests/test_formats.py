from datetime import datetime
from utils.formats import format_variations

def test_format_variations():
    dt = datetime(2024, 9, 1)
    formats = format_variations(dt)
    assert formats['YYYY-MM-DD'] == '2024-09-01'
    assert formats['YYYY/MM/DD'] == '2024/09/01'
    assert formats['DD-MM-YYYY'] == '01-09-2024'
    assert formats['ISO'].startswith('2024-09-01')
