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
a, b = np.polyfit(x_data, y_data, 1)

plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, a * x_data + b, color='red', label='Approximation')
plt.xlabel('ID')
plt.ylabel('MT(ms)')
plt.title('Approximate straight line')

# 近似直線の方程式
equation = f"MT = {a:.3f}ID + {b:.3f}"
plt.text(np.median(x_data), np.min(y_data), equation, fontsize=12, color='black')
plt.legend()

plt.savefig('fitts/approximation.png', dpi=300, bbox_inches='tight')
plt.show()

f.close()
