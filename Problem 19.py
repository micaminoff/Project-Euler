import time
start_time = time.time()

month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday_iterator = 2  # 1: Mon, 2: Tue etc
first_sundays = 0

# Go through every year
for i in range(1901, 2001):
    day_max = 0
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        day_max += 1
    day_max += 365
    current_day = 1
    while current_day <= day_max:
        for month in month_lengths:
            month_length = month
            if day_max == 366 and month == 28:
                month_length += 1
            for j in range(month_length):
                if j == 0 and weekday_iterator == 7:
                    first_sundays += 1
                weekday_iterator += 1
                current_day += 1
                if weekday_iterator > 7:
                    weekday_iterator = 1

print(first_sundays)
print(time.time() - start_time)
