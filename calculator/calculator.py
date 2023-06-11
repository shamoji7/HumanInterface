# 図５の作成
# 各ボタン間の平均距離、IDを計算する。
# 実移動距離を計算する。
# 実入力時間を計算する。
# 時間の単位は全てms

# fitts/approximation.py より、MT = 176.386 * ID + 285.871 とする。
def make_mt(id):
    return 176.386 * id + 285.871

# 予測総入力時間 = M + 48 * MT
def total_ms(mt):
    return 6 * mt + M

# KLMより M = 1.2 s
M = 1200

# KLM を使用 ---------------------------------------
P = 1100
B = 100
total_klm = M + 6 * (P + B*2)



import csv
import math



# 各ボタン間平均距離を使用 -----------------------------
f = open('calculator/buttons.csv', 'r', encoding='utf-8')
buttons = csv.reader(f)
header = next(buttons)
width = int(header[1])
next(buttons)

# 要素毎にリストに振り分ける
start = []
number = []
operator =[]
equal = []
for b in buttons:
    if b[0] == 'START':
        start.append(b)
    elif b[0].isdigit() and int(b[0]) >= 0 and int(b[0]) <= 9:
        number.append(b)
    elif b[0] == '=':
        equal.append(b)
    else:
        operator.append(b)

# no1 start to num
for row in start:
    tmp = []
    for row2 in number:
        x = (int(row[1]) - int(row2[1]))**2
        y = (int(row[2]) - int(row2[2]))**2
        dis = math.sqrt(x + y)
        tmp.append(dis)
    total = sum(tmp)
    no1 = total/len(number)

# no2 num to num
tmp2 = []
for i in range(len(number)):
    for j in range(len(number)):
        if i != j:
            x = (int(number[i][1]) - int(number[j][1]))**2
            y = (int(number[i][2]) - int(number[j][2]))**2
            dis = math.sqrt(x + y)
            tmp2.append(dis)
no2 = sum(tmp2)/(len(number)-1)**2

# no3 num to ope
tmp3 = []
for row in number:
    for row2 in operator:
        x = (int(row[1]) - int(row2[1]))**2
        y = (int(row[2]) - int(row2[2]))**2
        dis = math.sqrt(x + y)
        tmp3.append(dis)
no3 = sum(tmp3)/(len(number) * len(operator))

# no4 ope to num
no4 = no3

# no5 num to equal
tmp4 = []
for row in equal:
    for row2 in number:
        x = (int(row[1]) - int(row2[1]))**2
        y = (int(row[2]) - int(row2[2]))**2
        dis = math.sqrt(x + y)
        tmp3.append(dis)
no5 = sum(tmp3)/(len(number) * len(equal))

ave = round((no1 + no2 + no3 + no4 + no5)/5, 3)
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

real_time = round(sum(time)/8, 3)
N2 = len(distance2)
total_real = round(sum(distance2)/N2, 3)
ID2 = round(math.log2((total_real/width) + 1), 3)
MT2 = round(make_mt(ID2), 3)
TOTAL2 = round(total_ms(MT2), 3)


# 表示 ----------------------------------------
print('平均入力時間:', real_time, 'ms')
print('')
print('予測1 -----------------------------')
print('予測入力時間', total_klm, 'ms')
print('')
print('予測2 -----------------------------')
print('各ボタン間平均移動距離:', ave)
print('ID:', ID)
print('予測MT:', MT, 'ms')
print('予測入力時間:', TOTAL, 'ms')
print('')
print('予測3 -----------------------------')
print('平均実移動距離:', total_real)
print('ID:', ID2)
print('予測MT:', MT2, 'ms')
print('予測入力時間:', TOTAL2, 'ms')


f.close()
f2.close()