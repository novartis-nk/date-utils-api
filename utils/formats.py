from datetime import datetime


def format_variations(date: datetime) -> dict:
    return {
        "YYYY-MM-DD": date.strftime('%Y-%m-%d'),
        "YYYY/MM/DD": date.strftime('%Y/%m/%d'),
        "DD-MM-YYYY": date.strftime('%d-%m-%Y'),
        "DD/MM/YYYY": date.strftime('%d/%m/%Y'),
        "Full": date.strftime('%A, %d %B %Y'),
        "ISO": date.isoformat()
    }
