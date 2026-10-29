import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 1. 折线图：15天气温
days = list(range(1, 16))
date_label = ['9/4','9/5','9/6','9/7','9/8','9/9','9/10','9/11','9/12','9/13','9/14','9/15','9/16','9/17','9/18']
max_temp = [32,33,34,34,33,31,30,29,30,29,26,23,21,25,31]
min_temp = [19,19,20,22,22,21,22,16,18,18,17,14,15,16,16]
# 2. 柱状图：GDP
years = ['2018','2019','2020','2021','2022']
gdp = [919281,986515,1013567,1143670,1210207]
# 3. 散点图：速度-制动距离
speed = [10,20,30,40,50,60,70,80,90,100]
brake_dist = [5,10,16,24,35,48,63,80,99,120]
# 4. 饼图：粮食产量
grain_labels = ['稻谷','小麦','玉米','大豆','薯类','其他']
grain_yield = [21700,13800,27700,2030,3100,1200]
grain_colors = ['#FF9999','#66B3FF','#99FF99','#FFCC99','#C2C2F0','#FFB3E6']
# ---------------------- 2×2子图 ----------------------
fig, axes = plt.subplots(2,2,figsize=(14,10))
fig.suptitle('Matplotlib 综合可视化作业',fontsize=18,fontweight='bold')
plt.subplots_adjust(wspace=0.3,hspace=0.4)
# 子图1 折线图
ax1 = axes[0,0]
ax1.plot(days,max_temp,'r-o',lw=2,ms=6,label='最高温')
ax1.plot(days,min_temp,'b--s',lw=2,ms=6,label='最低温')
ax1.set_title('未来15天气温趋势')
ax1.set_xlabel('日期')
ax1.set_ylabel('温度(℃)')
ax1.set_xticks(days)
ax1.set_xticklabels(date_label,rotation=45)
ax1.legend()
ax1.grid(linestyle='--',alpha=0.6)
# 子图2 柱状图
ax2 = axes[0,1]
ax2.bar(years,gdp,color='#2E8B57',width=0.6)
ax2.set_title('2018-2022年GDP')
ax2.set_xlabel('年份')
ax2.set_ylabel('GDP(亿元)')
ax2.grid(axis='y',linestyle='--',alpha=0.6)
# 子图3 散点图
ax3 = axes[1,0]
ax3.scatter(speed,brake_dist,color='purple',marker='^',s=90,alpha=0.8)
ax3.set_title('汽车速度与制动距离')
ax3.set_xlabel('速度(km/h)')
ax3.set_ylabel('制动距离(m)')
ax3.grid(linestyle='--',alpha=0.6)
# 子图4 饼图
ax4 = axes[1,1]
ax4.pie(grain_yield,labels=grain_labels,colors=grain_colors,autopct='%1.1f%%',startangle=90)
ax4.set_title('2023年粮食产量占比')
plt.show()