
"""
implementing a program which allows someone to follow the amount they
jog in a certain time period. On the other hand, too much exercise can be bad,
so it is good to have reserved days for resting. Not too many days in a row
though.
"""


def main():
    days = input('Enter the number of days: ')

    consecutive_lazy_days = 0
    # lazy_days_resetter = 0
    total_distance = 0

    for x in range(1, int(days) + 1):
        kilometers = float(input("Enter day " + str(x) + " running length: "))
        if kilometers <= 0:
            consecutive_lazy_days += 1
        else:
            # lazy_days_resetter = 1
            consecutive_lazy_days = 0
            total_distance += float(kilometers)
        if consecutive_lazy_days == 3:
            print(
                "\nYou had too many consecutive lazy days!")

            break

    mean = total_distance / int(days)
    if consecutive_lazy_days < 3:
        if mean <= 3.00:
            print("\nYour running mean of %.2f km was too low!" % mean)
        else:
            print(
                "\nYou were persistent runner! With a mean of %.2f km." % mean)


if __name__ == "__main__":
    main()
