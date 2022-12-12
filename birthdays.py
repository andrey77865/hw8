from datetime import datetime, timedelta

users = [{"Bill": datetime(year=1980, month=12, day=16)}, {"Jina": datetime(year=1980, month=12, day=12)}, {
    "Adam": datetime(year=1980, month=12, day=13)}, {"Jason": datetime(year=1980, month=12, day=11)}, {"Kate": datetime(year=1980, month=12, day=16)}, {"Anna": datetime(year=1980, month=12, day=14)}]


def get_birthdays_per_week(users):
    result = ""
    bdays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    }
    today = datetime.now().date()
    offset = (today.weekday() - 5) % 7  # Date of the previous Saturday
    start_date = today - timedelta(days=offset)  # Previous Saturday
    end_date = start_date + timedelta(days=6)  # Future Friday

    while (start_date <= end_date):
        for dict in users:
            for name, bday in dict.items():
                if start_date.strftime('%m-%d') == bday.strftime('%m-%d'):
                    bday_day = datetime(
                        year=today.year, month=bday.month, day=bday.day).strftime('%A')
                    if bday_day == "Saturday" or bday_day == "Sunday":
                        bdays["Monday"].append(name)
                    else:
                        bdays[bday_day].append(name)
        start_date += timedelta(days=1)

    for day, names in bdays.items():
        if len(names) == 0:
            continue
        result += f"{day}: {', '.join(str(name) for name in names)} \n"

    return result


print(get_birthdays_per_week(users))
