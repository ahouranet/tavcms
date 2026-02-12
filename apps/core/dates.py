from datetime import datetime


def _to_jalali(gy: int, gm: int, gd: int) -> tuple[int, int, int]:
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    gy2 = gy + 1 if gm > 2 else gy
    days = (
        355666
        + (365 * gy)
        + ((gy2 + 3) // 4)
        - ((gy2 + 99) // 100)
        + ((gy2 + 399) // 400)
        + gd
        + g_d_m[gm - 1]
    )
    jy = -1595 + (33 * (days // 12053))
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if days < 186:
        jm = 1 + (days // 31)
        jd = 1 + (days % 31)
    else:
        jm = 7 + ((days - 186) // 30)
        jd = 1 + ((days - 186) % 30)
    return jy, jm, jd


def _format_gregorian(dt: datetime, include_time: bool) -> str:
    return dt.strftime("%Y-%m-%d %H:%M" if include_time else "%Y-%m-%d")


def _format_jalali(dt: datetime, include_time: bool) -> str:
    jy, jm, jd = _to_jalali(dt.year, dt.month, dt.day)
    date_part = f"{jy:04d}-{jm:02d}-{jd:02d}"
    if include_time:
        return f"{date_part} {dt:%H:%M}"
    return date_part


def _format_hijri_basic(dt: datetime, include_time: bool) -> str:
    date_part = dt.strftime("%Y-%m-%d")
    if include_time:
        return f"{date_part} {dt:%H:%M}"
    return date_part


def format_date(dt: datetime, lang: str) -> str:
    if lang == "fa":
        return _format_jalali(dt, include_time=False)
    if lang == "ar":
        return _format_hijri_basic(dt, include_time=False)
    return _format_gregorian(dt, include_time=False)


def format_datetime(dt: datetime, lang: str) -> str:
    if lang == "fa":
        return _format_jalali(dt, include_time=True)
    if lang == "ar":
        return _format_hijri_basic(dt, include_time=True)
    return _format_gregorian(dt, include_time=True)
