import matplotlib.pyplot as plt
import csv
import os

path = './fitts/csv'
flist = os.listdir(path)

namel = []
resultl = []
namel.append('Conditions')
resultl.append('Results')
for file in flist:
    # 全てのcsvファイルをまわる --------------------------
    csv_path = './fitts/csv/' + file
    f = open(csv_path, encoding='utf-8')
    csv_file = csv.reader(f)
    next(csv_file)
    filename = os.path.basename(csv_path)
    (basename, extension) = os.path.splitext(filename)

    timel = []
    for row in csv_file:
        timel.append(float(row[1]))
    namel.append(basename)
    resultl.append(sum(timel))
    

data = []
data.append(namel)
data.append(resultl)

fig, ax = plt.subplots()
ax.axis('off') 
table = ax.table(cellText=data, loc='center')

plt.savefig('fitts/table.png')
plt.show()