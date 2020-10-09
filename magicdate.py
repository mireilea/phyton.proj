def is_magic_date():
    print("running is magic date:")
    month = int(input('input month value: '))
    if (month >= 1) and (month <= 12):
        print()

    else:
        print("invalid month value")

    day = int(input('input day value:'))
    if (day >= 1) and (day <= 31):
        print()
    else:
        print("the day value must be 1 and 31 exclusive")

    year = int(input('input two digit year value:'))
    if (year >= 10) and (year <= 99):
        print()
    else:
        print("the year value must be positive and it must be two digit")

    if year is day * month:
        print("the date", month, day, year, "is magic")

    else:
        print("the date", month, day, year, "is not magic")

    is_magic_date()
