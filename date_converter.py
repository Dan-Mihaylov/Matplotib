import datetime


def convert_date(pd_timestamp):
    extract_date = str(pd_timestamp).split(" ")[0]
    year, month, day = extract_date.split("-")
    date = datetime.date(int(year), int(month), int(day))
    return date