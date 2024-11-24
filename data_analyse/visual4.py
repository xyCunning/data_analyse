import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
data = pd.read_excel('Cleaned_Combined.xlsx')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False    # 修复负号问题

# 设置绘图样式
sns.set_theme(style="whitegrid", font="SimHei", font_scale=1.2)

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制散点图
sns.scatterplot(data=data, x='面积/平方米', y='价格/元', color='blue', alpha=0.6, s=50, label="数据点", ax=ax)

# 绘制趋势线
sns.regplot(data=data, x='面积/平方米', y='价格/元', scatter=False, color='red', label="趋势线", ax=ax)

# 添加标题和标签
ax.set_title('租赁面积与价格的关系', fontsize=16)  # 使用 Axes 的 set_title
ax.set_xlabel('面积（平方米）', fontsize=12)
ax.set_ylabel('价格（元）', fontsize=12)
ax.legend(loc='upper left', fontsize=10)

# 保存并显示
plt.tight_layout()
box_plot_path = 'E:/qimodata/mine/picture/面积价格图.png'
plt.savefig(box_plot_path, dpi=300)
plt.show()

print(f"图像已保存至: {box_plot_path}")
