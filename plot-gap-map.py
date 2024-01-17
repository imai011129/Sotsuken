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
Gap from band 2 (0.3243498040853209) to band 3 (0.3261041257627011), 0.5394145832250122%
 This is Gap Checker. Radius is 0.13999999999999999
Gap from band 2 (0.33189884696348165) to band 3 (0.343177015093225), 3.34130392260892%
 This is Gap Checker. Radius is 0.15
Gap from band 2 (0.3407051529739591) to band 3 (0.36151572748939675), 5.927073687044436%
 This is Gap Checker. Radius is 0.16
Gap from band 2 (0.3499762116196901) to band 3 (0.38173571131854045), 8.68087527433427%
Gap from band 11 (0.6316172692327329) to band 12 (0.6327450214760163), 0.17839067988199164%
 This is Gap Checker. Radius is 0.17
Gap from band 2 (0.36179457607350074) to band 3 (0.4043711394981059), 11.114191762767774%
Gap from band 11 (0.6561942504973715) to band 12 (0.6637267397381071), 1.1413545653807446%
 This is Gap Checker. Radius is 0.18000000000000002
Gap from band 2 (0.3754715751571744) to band 3 (0.42975727950701326), 13.48329832826921%
Gap from band 11 (0.6847401070298115) to band 12 (0.6946745797316828), 1.4403895793214816%
 This is Gap Checker. Radius is 0.19000000000000003
Gap from band 2 (0.39086805493152144) to band 3 (0.4582625205054589), 15.8737578232311%
Gap from band 11 (0.7181001444700176) to band 12 (0.7217624743426426), 0.5087054590867952%
 This is Gap Checker. Radius is 0.20000000000000004
Gap from band 2 (0.410479008930897) to band 3 (0.4901564152333234), 17.693598134087633%
Gap from band 11 (0.7527289438254555) to band 12 (0.7531329360824427), 0.05365595110381338%
 This is Gap Checker. Radius is 0.21000000000000005
Gap from band 2 (0.43318636148864864) to band 3 (0.5252375798169147), 19.20887289248514%
 This is Gap Checker. Radius is 0.22000000000000006
Gap from band 2 (0.4599391903286111) to band 3 (0.5641361964397463), 20.349479629609394%
 This is Gap Checker. Radius is 0.23000000000000007
Gap from band 2 (0.49457465691928687) to band 3 (0.6071036625875716), 20.428650301234185%
 This is Gap Checker. Radius is 0.24000000000000007
Gap from band 2 (0.5344420014927204) to band 3 (0.6518390851823569), 19.792456443637395%
 This is Gap Checker. Radius is 0.25000000000000006
Gap from band 2 (0.592770921587019) to band 3 (0.7010820932630148), 16.74242289237928%
 This is Gap Checker. Radius is 0.26000000000000006
Gap from band 2 (0.6583610220572332) to band 3 (0.7459297595136489), 12.471596140289213%
 This is Gap Checker. Radius is 0.2700000000000001
Gap from band 2 (0.7506744082251773) to band 3 (0.7858250962228208), 4.5754245798174535%
Gap from band 14 (1.2476238909999289) to band 15 (1.252267353591846), 0.37149316810983374%
 This is Gap Checker. Radius is 0.2800000000000001
 This is Gap Checker. Radius is 0.2900000000000001
 This is Gap Checker. Radius is 0.3000000000000001
 This is Gap Checker. Radius is 0.3100000000000001
 This is Gap Checker. Radius is 0.3200000000000001
 This is Gap Checker. Radius is 0.3300000000000001
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