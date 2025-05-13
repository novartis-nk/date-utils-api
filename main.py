from fastapi import FastAPI, HTTPException, Query
from datetime import datetime

import jdatetime

from pydantic import BaseModel

from utils.converters import gregorian_to_jalali, jalali_to_gregorian
from utils.formats import format_variations
from utils.calendar_info import (
    get_all_days_of_month,
    get_all_days_of_jalali_month,
    get_weekends,
    get_month_name_gregorian,
    get_month_name_jalali,
)
from utils.next_dates import get_next_day, get_next_month, get_next_year

app = FastAPI()

class DateInfoResponse(BaseModel):
    input_date_gregorian: str
    input_date_jalali: str
    format_variants: dict
    all_days_gregorian: list
    all_days_jalali: list
    weekends: list
    month_name_gregorian: str
    month_name_jalali: str
    next_day: str
    next_month: str
    next_year: str


@app.get("/date-info", response_model=DateInfoResponse)
def get_date_info(
    date: str = Query(..., description="Date in format YYYY-MM-DD"),
    calendar: str = Query(..., enum=["gregorian", "jalali"],description="Specify the calendar type (gregorian or jalali)")
):
    try:
    # Validate the calendar parameter
        if calendar == "jalali":
            # Convert from Jalali to Gregorian if calendar is Jalali
            base_date = jalali_to_gregorian(date)
        else:
            # Otherwise, assume it's Gregorian and parse the date
            base_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date: {e}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing date: {e}")

    # Now that we have the Gregorian date, convert to Jalali for the response
    j_date = gregorian_to_jalali(base_date)
    return {
        "input_date_gregorian": base_date.strftime('%Y-%m-%d'),
        "input_date_jalali": j_date,
        "format_variants": format_variations(base_date),
        "all_days_gregorian": get_all_days_of_month(base_date),
        "all_days_jalali": get_all_days_of_jalali_month(jdatetime.date.fromgregorian(date=base_date)),
        "weekends": get_weekends(base_date),
        "month_name_gregorian": get_month_name_gregorian(base_date),
        "month_name_jalali": get_month_name_jalali(base_date),
        "next_day": get_next_day(base_date).strftime('%Y-%m-%d'),
        "next_month": get_next_month(base_date).strftime('%Y-%m-%d'),
        "next_year": get_next_year(base_date).strftime('%Y-%m-%d'),
    }
