#不同种类留言占比
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号


# 读取CSV文件，假设文件名为data.csv，并且第三列是留言类型字段
df = pd.read_csv('merged_UTF_8.csv')

# 提取第三列的数据
message_types = df.iloc[:, 2]

# 统计每种留言类型的数量
message_counts = message_types.value_counts()

# 不同明度的中国红色列表
china_red_colors = ['#dd2a29', '#e9786e', '#a8b5bd']
alpha_values = [0.5, 0.7, 0.9]

# 创建饼图
plt.figure(figsize=(8, 8))

for i in range(len(message_counts)):
    plt.pie(message_counts, labels=message_counts.index, autopct='%1.1f%%', startangle=140,
            colors=china_red_colors)
plt.title("不同种类留言占比")
plt.axis('equal')  # 保持饼图的纵横比相等
plt.show()


##########不同领域留言占比############
df = pd.read_csv('merged_UTF_8.csv')

# 提取第三列的数据
message_types = df.iloc[:, 3]

# 统计每种留言类型的数量
message_counts = message_types.value_counts()

# 不同明度的中国红色列表
china_red_colors = ['#dd2a29', '#e9786e', '#a8b5bd']
alpha_values = [0.5, 0.7, 0.9]

# 创建柱状图
plt.figure(figsize=(10, 6))
x = range(len(message_counts))

for i, (message_type, count) in enumerate(message_counts.items()):
    plt.bar(x[i], count, color=china_red_colors[i % len(china_red_colors)], alpha=alpha_values[i % len(alpha_values)])
    plt.text(x[i], count + 5, f'{count}', ha='center', va='bottom', fontsize=12, fontweight='bold')

# 设置x轴标签和标题
plt.xlabel("留言类型")
plt.ylabel("数量")
plt.title("不同种类留言的数量统计", fontsize=16, fontweight='bold')

# 设置x轴刻度和标签
plt.xticks(x, message_counts.index)

plt.show()


#留言与季节的关系
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件，假设文件名为data.csv
df = pd.read_csv('merged_UTF_8.csv')

# 将日期时间字段（假设字段名为'字段6'）转换为日期时间格式
df['字段6'] = pd.to_datetime(df['字段6'])

# 定义一个函数来确定季节
def get_season(month):
    if 3 <= month <= 5:
        return '春季'
    elif 6 <= month <= 8:
        return '夏季'
    elif 9 <= month <= 11:
        return '秋季'
    else:
        return '冬季'

# 通过字段6获取季节信息并创建新的季节列
df['季节'] = df['字段6'].dt.month.apply(get_season)

# 统计不同季节和留言类型的数量
season_message_counts = df.groupby(['季节', '字段4']).size().unstack(fill_value=0)

# 创建堆积柱状图
season_message_counts.plot(kind='bar', stacked=True, figsize=(12, 6))

# 设置图表标题和标签
plt.title("不同季节不同类型留言数量", fontsize=16, fontweight='bold')
plt.xlabel("季节")
plt.ylabel("留言数量")

# 显示图例
plt.legend(title="留言类型", title_fontsize=12)

# 显示图表
plt.show()


#各地区回复群众留言回复率
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件，假设文件名为data.csv
df = pd.read_csv('merged_UTF_8.csv')

# 根据字段8是否为空来判断是否已回复，并创建新的回复标志列
df['已回复'] = df['字段8'].notna()

# 定义函数来提取所属城市
def extract_city(region):
    parts = region.split('市')
    if len(parts) >= 2:
        return parts[0] + '市'
    return region

# 使用提取函数来创建新的城市列
df['城市'] = df['地区'].apply(extract_city)

# 按城市计算回复率
reply_rates = df.groupby('城市')['已回复'].mean() * 100

# 创建柱状图
plt.figure(figsize=(12, 6))
x = range(len(reply_rates))

plt.bar(x, reply_rates, color='blue', alpha=0.7)

# 设置x轴标签和标题
plt.xlabel("城市")
plt.ylabel("回复率 (%)")
plt.title("各城市回复群众留言回复率", fontsize=16, fontweight='bold')

# 设置x轴刻度和标签
plt.xticks(x, reply_rates.index, rotation=45)

# 在柱状图上添加数据标签
for i, rate in enumerate(reply_rates):
    plt.text(x[i], rate + 1, f'{rate:.2f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.show()




#地区办理留言平均用时
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件，假设文件名为data.csv
df = pd.read_csv('merged_UTF_8.csv')

# 将字段6和字段9转换为日期时间格式
df['字段6'] = pd.to_datetime(df['字段6'])
df['字段9'] = pd.to_datetime(df['字段9'], format='%Y-%m-%d %H:%M', errors='coerce')  # 转换为日期时间格式

# 计算每个留言的办理用时（字段9 - 字段6），并将结果存储在新列中
df['办理用时'] = (df['字段9'] - df['字段6']).dt.total_seconds() / 3600  # 将时间差转换为小时

# 定义函数来提取所属城市
def extract_city(region):
    parts = region.split('市')
    if len(parts) >= 2:
        return parts[0] + '市'
    return region
df['城市'] = df['地区'].apply(extract_city)
# 按地区计算办理留言的平均用时
average_processing_time = df.groupby('城市')['办理用时'].mean()

# 创建柱状图
plt.figure(figsize=(12, 6))
x = range(len(average_processing_time))

plt.bar(x, average_processing_time, color='green', alpha=0.7)

# 设置x轴标签和标题
plt.xlabel("地区")
plt.ylabel("平均办理用时 (小时)")
plt.title("各地区留言平均办理用时", fontsize=16, fontweight='bold')

# 设置x轴刻度和标签
plt.xticks(x, average_processing_time.index, rotation=45)

# 在柱状图上添加数据标签
for i, time in enumerate(average_processing_time):
    plt.text(x[i], time + 0.1, f'{time:.2f} 小时', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.show()

