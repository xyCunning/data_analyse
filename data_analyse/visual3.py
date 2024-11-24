import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('Cleaned_Combined.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 分组计算每个地铁距离区间的平均价格
grouped_data = df.groupby('地铁距离')['价格/元'].mean().reset_index()

# 折线图：地铁距离区间的平均价格
plt.figure(figsize=(12, 6))
plt.plot(grouped_data['地铁距离'], grouped_data['价格/元'], marker='o', linestyle='-', color='green')

# 添加标题和坐标轴标签
plt.title('不同地铁距离区间的平均价格趋势', fontsize=16)
plt.xlabel('地铁距离区间（米）', fontsize=12)
plt.ylabel('平均价格（元）', fontsize=12)

# 显示图形
box_plot_path = 'E:/qimodata/mine/picture/地铁图.png'
plt.tight_layout()
plt.savefig(box_plot_path)
plt.show()

print(f"箱线图已保存至: {box_plot_path}")