import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
df = pd.read_excel('Cleaned_Combined.xlsx')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建总楼层的分组
def categorize_total_floors(total_floor):
    if total_floor <= 6:
        return '1-6层'
    elif total_floor <= 12:
        return '7-12层'
    else:
        return '13层及以上'

df['总楼层区间'] = df['总楼层'].apply(categorize_total_floors)

# 绘制箱线图
plt.figure(figsize=(12, 6))
sns.boxplot(
    data=df,
    x='总楼层区间',
    y='价格/元',
    hue='总楼层区间',  # 用不同颜色区分总楼层区间
    palette='Set2'
)

# 设置标题和标签
plt.title('不同总楼层区间下当前楼层的价格分布', fontsize=16)
plt.xlabel('总楼层区间', fontsize=14)
plt.ylabel('价格（元）', fontsize=14)
plt.legend(title='总楼层区间', loc='upper right', fontsize=10)

# 保存箱线图
box_plot_path = 'E:/qimodata/mine/picture/楼层图.png'
plt.tight_layout()
plt.savefig(box_plot_path)
plt.show()

print(f"箱线图已保存至: {box_plot_path}")

