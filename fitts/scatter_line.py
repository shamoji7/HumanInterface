import csv
import matplotlib.pyplot as plt
import numpy as np


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

x_data = np.array(x_sorted, dtype=float)
y_data = np.array(y_sorted, dtype=float)
a, b = np.polyfit(x_data, y_data, 1)


plt.scatter(x_sorted, y_sorted)
plt.title('SCATTER PLOT')
plt.xlabel('ID')
plt.ylabel('MT (ms)')
plt.xticks(rotation=45)
plt.locator_params(axis='x', nbins=8)
plt.subplots_adjust(bottom=0.15, left=0.15)
plt.plot(x_data, a * x_data + b, color='red', label='Approximation')
equation = f"y = {a:.3f}x + {b:.3f}"
plt.text(np.min(x_data), np.max(y_data), equation, fontsize=12, color='black')
plt.legend()

# 散布図をpngで保存
#plt.savefig('./fitts/scatter_line.png')

f.close()
plt.show()
