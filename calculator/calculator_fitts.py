# 各ボタン間の平均距離、IDを計算する。
# 実移動距離を計算する。
# 実入力時間を計算する。
# 時間の単位は全てms

# fitts/approximation.py より、MT = 176.386 * ID + 285.871 とする。
def make_mt(id):
    return 176.386 * id + 285.871

# 予測総入力時間 = M + 48 * MT
def total_ms(mt):
    return 48 * mt + M * 8

# KLMより M = 1.2 s
M = 1200

# KLM を使用 ---------------------------------------
P = 1100
B = 100
klm = M + 6 * (P + B*2)
total_klm = 8 * klm



import csv
import math



# 各ボタン間平均距離を使用 -----------------------------
f = open('calculator/buttons.csv', 'r', encoding='utf-8')
buttons = csv.reader(f)
header = next(buttons)
width = int(header[1])
next(buttons)
N = 17
pairb = {}
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
    pairb[list[i][0]] = 0
    pairb[list[i][0]] = distance

total = sum(pairb.values())
ave = round(total/len(pairb), 3)
ID = round(math.log2((ave/width) + 1), 3)
MT = round(make_mt(ID), 3)
TOTAL = round(total_ms(MT), 3)


# 実移動距離を使用 ----------------------------------------
f2 = open('calculator/log.csv', 'r', encoding='utf-8')
log = csv.reader(f2)
next(log)
distance2 = []
time = []

for row in log:
    distance2.append(int(row[2]))
    time.append(int(row[1]))

real_time = round(sum(time), 3)
N2 = len(distance2)
total_real = round(sum(distance2)/N2, 3)
ID2 = round(math.log2((total_real/width) + 1), 3)
MT2 = round(make_mt(ID2), 3)
TOTAL2 = round(total_ms(MT2), 3)


# 表示 ----------------------------------------
print('KLM から予測 --------------------------')
print(total_klm, 'ms')
print('')
print('実総入力時間:', real_time, 'ms')
print('')
print('各ボタン間平均移動距離 から予測 -----------')
print('各ボタン間平均移動距離:', ave)
print('ID:', ID)
print('予測MT:', MT, 'ms')
print('予測総入力時間:', TOTAL, 'ms')
print('')
print('平均実移動距離 から予測 ------------------')
print('平均実移動距離:', total_real)
print('ID:', ID)
print('予測MT:', MT2, 'ms')
print('予測総入力時間:', TOTAL2, 'ms')


f.close()
f2.close()