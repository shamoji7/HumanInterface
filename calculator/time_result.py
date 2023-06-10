#

import csv

f = open('calculator/log.csv', encoding='utf-8')
log = csv.reader(f)

next(log)

time = []
for row in log:
    time.append(int(row[1]))

total_time = sum(time)
print('calculator time sum:', total_time, 'ms')
