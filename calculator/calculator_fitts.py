# 各ボタン間の平均距離、IDを計算する。
# 実移動距離を計算する。
# 実入力時間を計算する。

import csv
import math

f = open('calculator/buttons.csv', 'r', encoding='utf-8')
buttons = csv.reader(f)
header = next(buttons)
width = int(header[1])
next(buttons)
N = 17
pair = {}
list = []

for row in buttons:
    list.append(row)

for i in range(N):
    distance_box = []
    for j in range(N):
        if i != j:
            tmp1 = (int(list[i][1]) - int(list[j][1]))**2
            tmp2 = (int(list[i][2]) - int(list[j][2]))**2
            tmp3 = math.sqrt(tmp1 + tmp2)
            distance_box.append(tmp3)
    n = len(distance_box)
    d = 0
    for dis in distance_box:
        d += dis
    distance = d/n
    pair[list[i][0]] = 0
    pair[list[i][0]] = distance

total = sum(pair.values())
ave = total/len(pair)
ID = round(math.log2((ave/width) + 1), 3)


print('Calculator_ID:', ID)

f.close()