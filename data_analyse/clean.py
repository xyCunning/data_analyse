import pandas as pd

# 加载 Excel 文件
df = pd.read_excel('Combined.xlsx')  # 加载整个 Excel 文件
df = df.drop_duplicates()  # 1. 删除重复值
df['价格'] = pd.to_numeric(df['价格'], errors='coerce')  # 将非数值内容转换为 NaN
df['面积'] = pd.to_numeric(df['面积'], errors='coerce')

# 处理缺失值
# 数值列用中位数填充，文本列用最常见值填充
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:  # 数值列
        df[col] = df[col].fillna(df[col].median())  # 用中位数填充
    elif df[col].dtype == 'object':  # 文本列
        df[col] = df[col].fillna(df[col].mode()[0])  # 用最常见值填充

# 标准化楼层信息（拆分为当前楼层和总楼层）
df[['当前楼层', '总楼层']] = df['楼层'].str.extract(r'(\d+)/(\d+)').astype(float)

# 提取地铁信息中的距离和线路
df['地铁距离'] = df['地铁'].str.extract(r'距.*?站(\d+)米').astype(float)  # 提取距离
df['地铁线路'] = df['地铁'].str.extract(r'距(.*?站)').iloc[:, 0]  # 提取线路信息

df = df.drop(columns=['楼层'])
df = df.drop(columns=['地铁'])
# 清洗异常值
# 基于 IQR（四分位数间距）规则
for col in df.select_dtypes(include=['float64', 'int64']).columns:  # 仅处理数值列
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]  # 筛选正常值

# 重命名列
df = df.rename(columns={'价格': '价格/元', '面积': '面积/平方米', '位置1': '县区', '位置2': '具体位置'})

# 保存清洗后的数据
output_path = 'Cleaned_Combined.xlsx'
df.to_excel(output_path, index=False)
print(f"清洗后的数据已保存至: {output_path}")