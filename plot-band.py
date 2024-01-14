import pandas as pd
import matplotlib.pyplot as plt


e_file = 'band.xlsx'
df = pd.read_excel(e_file, sheet_name='Yablonovite')
# col_k_index には、k indexの列のアイテムが配列形式で入る
k_index = df['k index'].values
datas = {
    **{'band {}'.format(i): df['band {}'.format(i)].values for i in range(1, 17)}
}

# グラフをプロットする
plt.figure(figsize=(10, 5))

# 各bandについてプロットする
for col in datas:
    plt.plot(k_index, datas[col])

plt.xlabel('k index', fontsize=14)
plt.ylabel('Band Value', fontsize=14, fontstyle='italic', fontname='Times New Roman')
plt.legend()
plt.grid(True)
plt.show()