from datetime import datetime, timedelta, timezone


def get_msk_time(date: str):

    dt_utc = datetime.fromisoformat(date.replace("Z", "+00:00"))
    moscow_time = dt_utc.astimezone(timezone(timedelta(hours=3)))
    return moscow_time.strftime("%-d %B %Y года, %H:%M (МСК)")
