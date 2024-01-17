# matplotlibとcsvモジュールでcsvファイルのグラフを作成
import csv
import numpy as np
import matplotlib.pyplot as plt

# filename = input('Enter the filename: ')
filenames = [
    "./datas/inv_opals/e-10.csv", 
    "./datas/inv_opals/e-13.csv", 
    "./datas/inv_opals/e-15.csv",
]
fig, ax = plt.subplots()


for filename in filenames:
    rows = []
    with open(filename) as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

    header = rows.pop(0)

    data = np.float_(np.array(rows).T)

    ax.plot(data[0], data[1], linestyle='solid', marker='o', markersize=5, label=filename)
ax.legend()
ax.set_xlabel(header[0], fontname="Times New Roman",
              fontsize=14, fontstyle="italic")
ax.set_ylabel(header[1], fontname="Times New Roman", fontsize=14)

plt.show()
