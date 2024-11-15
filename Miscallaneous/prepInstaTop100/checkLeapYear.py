
def check_leap_year(year: int):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


year = int(input("Enter year: "))

print("leap year" if check_leap_year(year) else "not a leap year")
