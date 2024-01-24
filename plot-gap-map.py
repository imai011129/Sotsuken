import matplotlib.pyplot as plt
import freq_data_process

# 与えられたデータ
# filename = input('Enter the filename: ')
structure = "woodpile"
file = 'datas/woodpile/2.gaps.e-15.dat'
f = open(file, 'r')
content = f.read()
f.close()
datas = freq_data_process.process_data(content)
plt.figure()
# r.append("Radius,Frequency-min,Frequency-max,Frequency-min,Frequency-max")

data_lines = []
for data in datas:
    # データを処理してリストに格納
    data_lines.append(data.split(","))
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    # y5 = []
    # y6 = []

    for line in data_lines:
        x.append(float(line[0]))
        y1.append(float(line[1]))
        y2.append(float(line[2]))
        y3.append(float(line[3]))
        y4.append(float(line[4]))
        # y5.append(float(line[5]))
        # y6.append(float(line[6]))
    # y1 < y2 の条件を満たすかどうかのブール値のリストを生成
    where_condition_1 = [y1_val < y2_val for y1_val, y2_val in zip(y1, y2)]
    where_condition_2 = [y3_val < y4_val for y3_val, y4_val in zip(y3, y4)]
    # where_condition_3 = [y5_val < y6_val for y5_val, y6_val in zip(y5, y6)]

    # グラフの描画
    plt.fill_between(x, y1, y2, color='#555555', where=where_condition_1)
    plt.fill_between(x, y3, y4, color='#555555', where=where_condition_2)
    # plt.fill_between(x, y5, y6, color='#555555', where=where_condition_3)
plt.xlabel('Width $w / a$', fontname='Times New Roman', fontsize=14)
plt.ylabel('Frequency $\omega a / 2 \pi c$',
           fontname='Times New Roman', fontsize=14)
# plt.legend()
plt.xlim(0, 0.7)
plt.ylim(0, 1)
plt.show()