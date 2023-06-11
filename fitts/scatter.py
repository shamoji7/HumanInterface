# 散布図と近似曲線を表示させる。
# 結果を aprroximation.png として保存する。


import numpy as np
import matplotlib.pyplot as plt
import csv

f = open('fitts/result.csv', encoding='utf-8')
result = csv.reader(f)
next(result)

ID = []
MT = []
for row in result:
    MT.append(row[1])
    ID.append(row[2])

x_data = np.array(ID, dtype=float)
y_data = np.array(MT, dtype=float)

plt.scatter(x_data, y_data, label='Data')
plt.xlabel('ID')
plt.ylabel('MT(ms)')
plt.title('Scatter')

plt.savefig('fitts/scatter.png', dpi=300, bbox_inches='tight')
plt.show()

f.close()
