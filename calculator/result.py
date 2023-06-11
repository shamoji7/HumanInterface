# 8回のタスクの入力時間を出力する
# 表3の作成

import csv

f = open('calculator/log.csv', 'r')
log = csv.reader(f)
next(log)

time_pair = {}
counter = 0
for data in log:
    judge = counter//6 + 1
    if judge not in time_pair:
        time_pair[judge] = 0
        time_pair[judge] = int(data[1])
    else:
        tmp = time_pair[judge]
        tmp += int(data[1])
        time_pair[judge] = tmp
    counter += 1

print(time_pair)

