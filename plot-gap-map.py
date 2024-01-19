import matplotlib.pyplot as plt
import freq_data_process

# 与えられたデータ
# Yablonovite e-15
colors = ["blue", "orange", "green", "red"]
d = """ 
 This is Gap Checker. Radius is 0
 This is Gap Checker. Radius is 0.01
 This is Gap Checker. Radius is 0.02
 This is Gap Checker. Radius is 0.03
 This is Gap Checker. Radius is 0.04
 This is Gap Checker. Radius is 0.05
 This is Gap Checker. Radius is 0.060000000000000005
 This is Gap Checker. Radius is 0.07
 This is Gap Checker. Radius is 0.08
 This is Gap Checker. Radius is 0.09
 This is Gap Checker. Radius is 0.09999999999999999
 This is Gap Checker. Radius is 0.10999999999999999
 This is Gap Checker. Radius is 0.11999999999999998
 This is Gap Checker. Radius is 0.12999999999999998
 This is Gap Checker. Radius is 0.13999999999999999
 This is Gap Checker. Radius is 0.15
 This is Gap Checker. Radius is 0.16
 This is Gap Checker. Radius is 0.17
 This is Gap Checker. Radius is 0.18000000000000002
 This is Gap Checker. Radius is 0.19000000000000003
Gap from band 2 (0.42017304654452975) to band 3 (0.42516063754745503), 1.180028927460215%
 This is Gap Checker. Radius is 0.20000000000000004
Gap from band 2 (0.4307518041311751) to band 3 (0.45166036484833677), 4.738955660899809%
 This is Gap Checker. Radius is 0.21000000000000005
Gap from band 2 (0.4401806928111336) to band 3 (0.47518644872837024), 7.648462420960941%
 This is Gap Checker. Radius is 0.22000000000000006
Gap from band 2 (0.4500911320170875) to band 3 (0.49865875282632643), 10.238234878364123%
 This is Gap Checker. Radius is 0.23000000000000007
Gap from band 2 (0.46084857991621947) to band 3 (0.5224817056153838), 12.535589843212138%
 This is Gap Checker. Radius is 0.24000000000000007
Gap from band 2 (0.47295114245408) to band 3 (0.5469964183459831), 14.519428005459583%
 This is Gap Checker. Radius is 0.25000000000000006
Gap from band 2 (0.486687035434546) to band 3 (0.5722634768340166), 16.162500590540787%
 This is Gap Checker. Radius is 0.26000000000000006
Gap from band 2 (0.502199855363918) to band 3 (0.5978918579861536), 17.397095435039333%
 This is Gap Checker. Radius is 0.2700000000000001
Gap from band 2 (0.5202879237117841) to band 3 (0.6242642939979772), 18.1689168353103%
 This is Gap Checker. Radius is 0.2800000000000001
Gap from band 2 (0.5415026792189146) to band 3 (0.6506864562917186), 18.31651938784678%
 This is Gap Checker. Radius is 0.2900000000000001
Gap from band 2 (0.5668517926487513) to band 3 (0.6769860562002551), 17.708781518976494%
 This is Gap Checker. Radius is 0.3000000000000001
Gap from band 2 (0.5981615708799461) to band 3 (0.7028228623274961), 16.08955323001343%
 This is Gap Checker. Radius is 0.3100000000000001
Gap from band 2 (0.6379537553736101) to band 3 (0.7282786239099159), 13.222475166878073%
 This is Gap Checker. Radius is 0.3200000000000001
Gap from band 2 (0.6909536311274024) to band 3 (0.7534118313700795), 8.648531395188494%
 This is Gap Checker. Radius is 0.3300000000000001
Gap from band 2 (0.7660143711475144) to band 3 (0.7785146364696953), 1.6186507680377573%
 This is Gap Checker. Radius is 0.34000000000000014
 This is Gap Checker. Radius is 0.35000000000000014
 This is Gap Checker. Radius is 0.36000000000000015
 This is Gap Checker. Radius is 0.37000000000000016
 This is Gap Checker. Radius is 0.38000000000000017
 This is Gap Checker. Radius is 0.3900000000000002
 This is Gap Checker. Radius is 0.4000000000000002
 This is Gap Checker. Radius is 0.4100000000000002
 This is Gap Checker. Radius is 0.4200000000000002
 This is Gap Checker. Radius is 0.4300000000000002
 This is Gap Checker. Radius is 0.4400000000000002
 This is Gap Checker. Radius is 0.45000000000000023
 This is Gap Checker. Radius is 0.46000000000000024
 This is Gap Checker. Radius is 0.47000000000000025
 This is Gap Checker. Radius is 0.48000000000000026
 This is Gap Checker. Radius is 0.49000000000000027
 This is Gap Checker. Radius is 0.5000000000000002
 This is Gap Checker. Radius is 0.5100000000000002
 This is Gap Checker. Radius is 0.5200000000000002
 This is Gap Checker. Radius is 0.5300000000000002
 This is Gap Checker. Radius is 0.5400000000000003
 This is Gap Checker. Radius is 0.5500000000000003
 This is Gap Checker. Radius is 0.5600000000000003
 This is Gap Checker. Radius is 0.5700000000000003
 This is Gap Checker. Radius is 0.5800000000000003
 This is Gap Checker. Radius is 0.5900000000000003
 This is Gap Checker. Radius is 0.6000000000000003
 This is Gap Checker. Radius is 0.6100000000000003
 This is Gap Checker. Radius is 0.6200000000000003
 This is Gap Checker. Radius is 0.6300000000000003
 This is Gap Checker. Radius is 0.6400000000000003
 This is Gap Checker. Radius is 0.6500000000000004
 This is Gap Checker. Radius is 0.6600000000000004
 This is Gap Checker. Radius is 0.6700000000000004
 This is Gap Checker. Radius is 0.6800000000000004
 This is Gap Checker. Radius is 0.6900000000000004
 This is Gap Checker. Radius is 0.7000000000000004
 This is Gap Checker. Radius is 0.7100000000000004
 This is Gap Checker. Radius is 0.7200000000000004
 This is Gap Checker. Radius is 0.7300000000000004
 This is Gap Checker. Radius is 0.7400000000000004
 This is Gap Checker. Radius is 0.7500000000000004
 This is Gap Checker. Radius is 0.7600000000000005
 This is Gap Checker. Radius is 0.7700000000000005
 This is Gap Checker. Radius is 0.7800000000000005
 This is Gap Checker. Radius is 0.7900000000000005
 This is Gap Checker. Radius is 0.8000000000000005
 This is Gap Checker. Radius is 0.8100000000000005
 This is Gap Checker. Radius is 0.8200000000000005
 This is Gap Checker. Radius is 0.8300000000000005
 This is Gap Checker. Radius is 0.8400000000000005
 This is Gap Checker. Radius is 0.8500000000000005
 This is Gap Checker. Radius is 0.8600000000000005
 This is Gap Checker. Radius is 0.8700000000000006
 This is Gap Checker. Radius is 0.8800000000000006
 This is Gap Checker. Radius is 0.8900000000000006
 This is Gap Checker. Radius is 0.9000000000000006
 This is Gap Checker. Radius is 0.9100000000000006
 This is Gap Checker. Radius is 0.9200000000000006
 This is Gap Checker. Radius is 0.9300000000000006
 This is Gap Checker. Radius is 0.9400000000000006
 This is Gap Checker. Radius is 0.9500000000000006
 This is Gap Checker. Radius is 0.9600000000000006
 This is Gap Checker. Radius is 0.9700000000000006
 This is Gap Checker. Radius is 0.9800000000000006
 This is Gap Checker. Radius is 0.9900000000000007
"""

datas = freq_data_process.process_data(d)
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
plt.xlabel('Radius $r / a$', fontname='Times New Roman', fontsize=14)
plt.ylabel('Frequency $\omega a / 2 \pi c$',
           fontname='Times New Roman', fontsize=14)
# plt.legend()
plt.xlim(0, 0.7)
plt.ylim(0, 1)
plt.show()