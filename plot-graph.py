# matplotlibとcsvモジュールでcsvファイルのグラフを作成
import csv
import numpy as np
import matplotlib.pyplot as plt

filename = input('Enter the filename: ')
path_csv = f"./datas/{filename}"
rows = []
with open(path_csv) as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

header = rows.pop(0)

data = np.float_(np.array(rows).T)


fig, ax = plt.subplots()

ax.plot(data[0], data[1], linestyle='solid', marker='o', color="#333333", markersize=5)

ax.set_xlabel(header[0], fontname="Times New Roman",
              fontsize=14, fontstyle="italic")
ax.set_ylabel(header[1], fontname="Times New Roman", fontsize=14)

plt.show()
