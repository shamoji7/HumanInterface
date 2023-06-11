# 演習2-1において、条件毎のMTとIDを求めてCSVとして保存


import csv
import os
import re
import math

path = './fitts/csv'
flist = os.listdir(path)

# 結果出力用csv ---------------------------------------
new = open('./fitts/result.csv', 'w', newline='')
writer = csv.writer(new)
writer.writerow(['filename', 'MT', 'ID'])

for file in flist:
    # 全てのcsvファイルをまわる --------------------------
    csv_path = './fitts/csv/' + file
    f = open(csv_path, encoding='utf-8')
    csv_file = csv.reader(f)
    next(csv_file)
    filename = os.path.basename(csv_path)
    (basename, extension) = os.path.splitext(filename)
    print(file)

    # W, Dをファイル名から取得し、IDを計算する ------------------
    pattern = r"d(\d+)w(\d+)"
    matches = re.findall(pattern, basename)
    for match in matches:  
        D = int(match[0])
        W = int(match[1])
    ID = math.log2((D/W) + 1)
    print('ID:', ID)

    # 平均選択時間を計算する
    MTi_list = []
    MT = 0
    counter = 0

    for row in csv_file:
        MTi = float(row[1])/13
        MTi_list.append(MTi)
    print("MTi_list", MTi_list)

    for mti in MTi_list:
        MT += mti
    print('MT:', MT)

    # csvに書き込み
    writer.writerow([filename, MT, ID])

new.close()
f.close()
