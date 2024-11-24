import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 加载数据
data = pd.read_excel('Cleaned_Combined.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False    # 修复负号问题
# 2. 计算每个房型的平均租金
avg_rent_per_type = data.groupby('户型')['价格/元'].mean().sort_values(ascending=False).reset_index()

# 3. 绘制柱状图
plt.figure(figsize=(10, 6))
sns.barplot(
    data=avg_rent_per_type,
    x='户型',
    y='价格/元',
    palette='coolwarm'  # 使用不同颜色
)

# 4. 添加标签和标题
plt.title('各户型的平均租金价格', fontsize=16)
plt.xlabel('户型', fontsize=12)
plt.ylabel('平均租金价格（元）', fontsize=12)

# 在柱状图顶部显示平均租金数值
for i, value in enumerate(avg_rent_per_type['价格/元']):
    plt.text(i, value + 10, f'{value:.0f}', ha='center', fontsize=10)

# 调整布局并显示图像
plt.tight_layout()

# 5. 保存图像
output_path = 'E:/qimodata/mine/picture/房型平均租金.png'
plt.savefig(output_path, dpi=300)
plt.show()

print(f"图像已保存至: {output_path}")
