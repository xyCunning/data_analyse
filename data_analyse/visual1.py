import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置支持中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False   # 解决负号显示问题

# 加载清洗后的 Excel 数据
df = pd.read_excel('Cleaned_Combined.xlsx')

# 统计每个区县的平均价格
average_price = df.groupby('县区')['价格/元'].mean().sort_values(ascending=False)

# 绘制柱状图
plt.figure(figsize=(12, 6))
average_price.plot(kind='bar', color='skyblue', edgecolor='black', alpha=0.8)

# 设置标题和标签
plt.title('各县区平均价格分布', fontsize=16)
plt.xlabel('县区', fontsize=14)
plt.ylabel('平均价格（元）', fontsize=14)

# 调整 x 轴标签角度，避免重叠
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)

# 添加数值标签到柱状图上
for index, value in enumerate(average_price):
    plt.text(index, value + 0.5, f'{value:.1f}', ha='center', fontsize=10)

# 保存柱状图
bar_chart_path = 'E:/qimodata/mine/picture/县区平均价格.png'
plt.tight_layout()  # 自动调整布局
plt.savefig(bar_chart_path)
plt.show()

print(f"柱状图已保存至: {bar_chart_path}")
