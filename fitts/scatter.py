# 散布図を表示させる。
# 結果を scatter.png として保存。


import csv
import matplotlib.pyplot as plt

f = open('./fitts/result.csv', encoding='utf-8')
results = csv.reader(f)
next(results)

ID = []
MT = []

for row in results:
    MT.append(row[1])
    ID.append(row[2])

MT_fixed = [f'{float(num):.3f}' for num in MT]
ID_fixed = [f'{float(num):.3f}' for num in ID]

x_sorted, y_sorted = zip(*sorted(zip(ID_fixed, MT_fixed)))
plt.scatter(x_sorted, y_sorted)

plt.title('SCATTER')
plt.xlabel('ID')
plt.ylabel('MT (ms)')
plt.xticks(rotation=45)
plt.locator_params(axis='x', nbins=8)
plt.subplots_adjust(bottom=0.15, left=0.15)


# 散布図をpngで保存
plt.savefig('./fitts/scatter.png')

f.close()
plt.show()
