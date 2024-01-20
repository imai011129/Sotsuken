# matplotlibとcsvモジュールでcsvファイルのグラフを作成
import csv
import numpy as np
import matplotlib.pyplot as plt
import freq_data_process

# filename = input('Enter the filename: ')
structure = "inv_opals"
files = [
    [f'datas/{structure}/gaps.e-5.dat', 'epsilon = 5'],
    [f'datas/{structure}/gaps.e-10.dat', 'epsilon = 10'],
    [f'datas/{structure}/gaps.e-13.dat', 'epsilon = 13'],
    [f'datas/{structure}/gaps.e-15.dat', 'epsilon = 15'],
]

fig, ax = plt.subplots()
for file in files:
    f = open(file[0], 'r')
    content = f.read()
    f.close()
    data_strings = freq_data_process.process_data(content)


    data = []
    for s in data_strings:
        parts = s.split(',')
        if all(p.strip() for p in parts):
            data.append(list(map(float, parts)))

    # 各列のデータを抽出
    widths = [row[0] for row in data]
    gap_min = [row[1] for row in data]
    gap_max = [row[2] for row in data]
    gap_midgap_ratio = []
    for i in range(len(gap_min)):
        if gap_max[i] == gap_min[i] == 0:
            gap_midgap_ratio.append(0)
        else:
            gap_midgap_ratio.append(100 * (gap_max[i] - gap_min[i]) / ((gap_max[i] + gap_min[i]) / 2))
    # グラフのプロット

    ax.plot(widths, gap_midgap_ratio, label=file[1], marker='o', markersize=4)


plt.xlabel('Width $w / a$')
plt.ylabel('Gap-midgap ratio (%)')
plt.legend()
plt.show()