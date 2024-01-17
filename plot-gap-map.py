import matplotlib.pyplot as plt

# データ例
# データ形式は以下の通り
# 面倒なので逐次データは手打ちしてください
# Radius r/a	Frequency-min ωa/2πc	Frequency-max ωa/2πc
# 0.000000	0.000000	0.000000
data = """

"""


# データを処理してリストに格納
data_lines = data.strip().split("\n")
ra = []
frequency_min = []
frequency_max = []

for line in data_lines[1:]:  # 最初の行はヘッダなのでスキップ
    values = line.split("\t")
    ra.append(float(values[0]))
    frequency_min.append(float(values[1]))
    frequency_max.append(float(values[2]))

# frequency-min と frequency-max が等しくないデータのみを抽出
filtered_ra = [x for x, min_val, max_val in zip(ra, frequency_min, frequency_max) if min_val != max_val]
filtered_frequency_min = [min_val for min_val, max_val in zip(frequency_min, frequency_max) if min_val != max_val]
filtered_frequency_max = [max_val for min_val, max_val in zip(frequency_min, frequency_max) if min_val != max_val]

# グラフの描画
plt.figure()
plt.fill_between(filtered_ra, filtered_frequency_min, filtered_frequency_max, color='blue', alpha=0.5)
plt.xlabel('Radius r/a')
plt.ylabel('Frequency ωa/2πc')
plt.title('TM-gap map')
plt.xlim(0, 0.7)  # x軸の範囲を0から0.7まで指定
plt.ylim(0, 1)    # y軸の範囲を0から1まで指定
plt.show()
