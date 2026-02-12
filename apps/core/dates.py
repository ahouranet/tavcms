from datetime import date, datetime


def _to_jalali(g_date: date) -> tuple[int, int, int]:
    gy = g_date.year - 1600
    gm = g_date.month - 1
    gd = g_date.day - 1

    g_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    j_days_in_month = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]

    g_day_no = 365 * gy + (gy + 3) // 4 - (gy + 99) // 100 + (gy + 399) // 400
    for i in range(gm):
        g_day_no += g_days_in_month[i]
    if gm > 1 and ((gy + 1600) % 4 == 0 and ((gy + 1600) % 100 != 0 or (gy + 1600) % 400 == 0)):
        g_day_no += 1
    g_day_no += gd

    j_day_no = g_day_no - 79
    j_np = j_day_no // 12053
    j_day_no %= 12053

    jy = 979 + 33 * j_np + 4 * (j_day_no // 1461)
    j_day_no %= 1461

    if j_day_no >= 366:
        jy += (j_day_no - 1) // 365
        j_day_no = (j_day_no - 1) % 365

    jm = 0
    for i in range(11):
        if j_day_no < j_days_in_month[i]:
            jm = i + 1
            break
        j_day_no -= j_days_in_month[i]
    else:
        jm = 12

    jd = j_day_no + 1
    return jy, jm, jd


def _to_hijri_approx(g_date: date) -> tuple[int, int, int]:
    days = (g_date - date(622, 7, 19)).days
    if days < 0:
        return g_date.year, g_date.month, g_date.day
    year = int(days / 354.367) + 1
    rem = days - int((year - 1) * 354.367)
    month = int(rem / 29.53) + 1
    if month > 12:
        month = 12
    day = rem - int((month - 1) * 29.53) + 1
    return year, month, day


def format_date(dt: date | datetime, lang: str) -> str:
    value = dt.date() if isinstance(dt, datetime) else dt
    if lang == "fa":
        y, m, d = _to_jalali(value)
        return f"{y:04d}/{m:02d}/{d:02d}"
    if lang == "ar":
        y, m, d = _to_hijri_approx(value)
        return f"{y:04d}/{m:02d}/{d:02d}"
    return value.strftime("%Y-%m-%d")


def format_datetime(dt: datetime, lang: str) -> str:
    date_part = format_date(dt, lang)
    return f"{date_part} {dt.strftime('%H:%M')}"
