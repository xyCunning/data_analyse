import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 用于获取调色板

# 读取 Excel 数据
data = pd.read_excel('Cleaned_Combined.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False    # 修复负号问题
# 按小区名称分组，计算平均租金
top10_communities = (
    data.groupby('小区')['价格/元']
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# 打印结果
print("出租金最贵的10个小区：")
print(top10_communities)

# 获取调色板
colors = sns.color_palette('husl', len(top10_communities))  # 使用 'husl' 调色板

# 绘制柱状图
plt.figure(figsize=(12, 6))
bars = plt.barh(top10_communities['小区'], top10_communities['价格/元'], color=colors)

# 添加文字标注（平均租金）
for bar, rent in zip(bars, top10_communities['价格/元']):
    plt.text(
        bar.get_width() + 10,  # X 坐标稍微超出柱图的宽度
        bar.get_y() + bar.get_height() / 2,  # Y 坐标为柱图的中心位置
        f'{rent:.2f}',  # 显示小数点后两位
        va='center',  # 垂直对齐到柱图中心
        fontsize=10
    )

# 设置标题和标签
plt.xlabel('平均租金（元）', fontsize=14)
plt.ylabel('小区名称', fontsize=14)
plt.title('出租金最贵的10个小区', fontsize=16)
plt.gca().invert_yaxis()  # 反转Y轴，使租金最高的小区显示在最上方
plt.tight_layout()

# 保存图片
output_path = 'E:/qimodata/mine/picture/最贵小区图.png'
plt.savefig(output_path)
plt.show()

print(f"图像已保存至: {output_path}")
