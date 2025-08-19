import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta

import requests  # type: ignore

DELIVERY_TIME = 2


def get_eta(purchase_date: date) -> date:
    holidays = get_holidays(2025)
    eta = purchase_date
    added_days = 0

    while added_days < DELIVERY_TIME:
        eta += timedelta(days=1)
        if eta not in holidays and eta.weekday() != 6:
            added_days += 1
    return eta


def get_holidays(year: int) -> list[date]:
    url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo"
    holidays = []
    for month in range(1, 13):
        params = {
            "serviceKey": "MG8isCfKhcNkQHsp3YWZfEIehP/I4vx0Tyn5JRs/res9oG8L0STwf+E+T2w2ToymdBZu4gXR2KDIFAG/wtFslQ==",
            "pageNo": "1",
            "numOfRows": "50",
            "solYear": "2025",
            "solMonth": f"{month:02d}",
        }
        res = requests.get(url, params=params)

        root = ET.fromstring(res.content)
        items = root.findall(".//item")

        for item in items:
            locdate = item.findtext("locdate")
            is_holiday = item.findtext("isHoliday")  # Y/N
            if locdate is None:
                continue

            if is_holiday == "Y":
                date = datetime.strptime(locdate, "%Y%m%d").date()
                holidays.append(date)
    return holidays


def test_2025_10_03() -> None:
    result = get_eta(datetime(2025, 10, 3).date())
    assert result == datetime(2025, 10, 10).date()
