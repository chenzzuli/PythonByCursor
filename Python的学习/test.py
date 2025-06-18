# 这是一个画图项目的测试
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
# 生成正态分布数据
data = stats.norm.rvs(loc=0, scale=1, size=1000)

print(data)
# 计算基本统计量
print("均值：", stats.tmean(data))
print("标准差：", stats.tstd(data))
print("偏度：", stats.skew(data))
print("峰度：", stats.kurtosis(data))

# 绘制直方图和核密度估计
plt.figure(figsize=(10, 6))
plt.hist(data, bins=50, density=True, alpha=0.7)
x = np.linspace(data.min(), data.max(), 100)
plt.plot(x, stats.norm.pdf(x, loc=0, scale=1))
plt.title('数据分布')
plt.show()
