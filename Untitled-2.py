import os
# 若不存在L8文件夹就自动新建
if not os.path.exists("L8"):
    os.mkdir("L8")
# 原有 render("L8/scatter.html") 代码不用改动
#!/usr/bin/env python
# coding: utf-8

# ## 8.1	pyecharts概述

# ### 8.1.2 认识Echarts


from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.globals import ThemeType
# 准备数据
data = [
    [10, 10, 10],
    [20, 20, 20],
    [30, 30, 30],
    [40, 40, 40],
    [50, 50, 50],
    [60, 60, 60],
]

# 绘制气泡图
scatter = (
    Scatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis([str(i) for i in range(1, len(data)+1)])
    .add_yaxis("气泡A", data, label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis("气泡B", [[i[0]+10, i[1]+10, i[2]+10] for i in data], label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="气泡图示例", subtitle="我是副标题"),
        legend_opts=opts.LegendOpts(is_show=True),
        visualmap_opts=opts.VisualMapOpts(
            type_="size", min_=10, max_=60, dimension=2, is_piecewise=True
        ),
        datazoom_opts=opts.DataZoomOpts(),
        toolbox_opts=opts.ToolboxOpts(
            feature={
                "saveAsImage": {},
                "dataZoom": {},
                "restore": {},
                "dataView": {},
                "magicType": {
                    "type": ["line"]  # 添加"line"和"bar"类型的切换按钮
                },
            },
            pos_right='1000',
        ),
    )
)
scatter.render('L8/scatter.html')


# ### 8.1.3 pyecharts数据集
from pyecharts.faker import Faker
print(Faker.fruits)

print(Faker.choose())   # 随机获取一组测试数据
print(Faker.values())   # 生成包含7个随机整数的列表


# ## 8.2	pyecharts初体验

# ### 8.2.1 绘制第一个图表

###普通写法（分步写）
# 1.导入所需的模块或类
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
# 2.创建图表类的对象
bar = Bar(init_opts=opts.InitOpts(width="600px", height="300px"))
# 3.添加数据和设置配置项
# 3.1 添加数据
bar.add_xaxis(Faker.clothes)
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90, 50])
# 3.2 设置全局配置项
bar.set_global_opts(title_opts=opts.TitleOpts(title="柱形图示例"), 
                        yaxis_opts=opts.AxisOpts(name="销售额(万元)", 
                        name_location="center", name_gap=30))
# 3.3 设置系列配置项
bar.set_series_opts(label_opts=opts.LabelOpts(position="top"))
# 4.渲染图表
bar.render('L8/bar1.html')

####链式写法（连起来写）
# 1.导入所需的模块或类
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
bar = (
    # 2.创建图表类的对象
    Bar(init_opts=opts.InitOpts(width="600px", height="300px"))
    # 3.添加数据和设置配置项
    # 3.1 添加数据
    .add_xaxis(Faker.clothes)
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90, 50])
    # 3.2 设置全局配置项
    .set_global_opts(title_opts=opts.TitleOpts(title="柱形图示例"),
                        yaxis_opts=opts.AxisOpts(name="销售额(万元)",
                        name_location="center", name_gap=30))
    # 3.3 设置系列配置项
    .set_series_opts(label_opts=opts.LabelOpts(position="top"))
)
# 4.渲染图表
bar.render('L8/bar2.html')


# ### 8.2.2 认识图表类
#给柱形图设置一张 “画布” 的大小：宽 600 像素、高 300 像素。
Bar(init_opts=opts.InitOpts(width="600px", height="300px"))

# ### 8.2.3 认识配置项
#设置全局配置项
bar.set_global_opts(title_opts=opts.TitleOpts(title="柱形图示例"),
                        yaxis_opts=opts.AxisOpts(name="销售额(万元)",
                        name_location="center", name_gap=30))

bar.set_series_opts(label_opts=opts.LabelOpts(position="top"))

#pyecharts中还可以通过创建字典的方式创建全局配置项和系列配置项，字典的键与全局配置项和系列配置项类中构造方法的参数名相同。
dict(position="top")         # 写法一
{"position": "top"}          # 写法二


# ### 8.2.4 渲染图表
bar.render_notebook()

####基于8.2.1解释
# 【导入模块】从pyecharts图表库中导入 柱形图(Bar) 类
from pyecharts.charts import Bar
# 【导入模块】从pyecharts内置测试数据集中导入Faker，用于快速获取演示数据
from pyecharts.faker import Faker
# 【导入模块】导入pyecharts配置项模块，并用别名opts简化调用
from pyecharts import options as opts
# ---------------------- 2. 创建图表对象 ----------------------
# 创建Bar柱形图对象，并初始化图表画布大小：宽600像素，高300像素
bar = Bar(init_opts=opts.InitOpts(width="600px", height="300px"))
# ---------------------- 3. 添加数据与配置项 ----------------------
# 3.1 添加图表数据
# 给X轴添加数据：使用Faker内置的服装名称列表作为X轴标签
bar.add_xaxis(Faker.clothes)
# 给Y轴添加数据：系列名称为“商家A”，后面列表是对应X轴的数值
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90, 50])
# 3.2 设置全局配置项（对整个图表生效：标题、坐标轴、图例等）
bar.set_global_opts(
    # 设置图表主标题
    title_opts=opts.TitleOpts(title="柱形图示例"),
    # 设置Y轴：轴名称为“销售额(万元)”，名称居中显示，名称与轴线间距30
    yaxis_opts=opts.AxisOpts(name="销售额(万元)", name_location="center", name_gap=30)
)
# 3.3 设置系列配置项（对当前数据系列生效：标签、颜色、标记等）
# 设置数据标签显示在柱子顶部
bar.set_series_opts(label_opts=opts.LabelOpts(position="top"))
# ---------------------- 4. 渲染并保存图表 ----------------------
# 将绘制好的柱形图保存到当前目录下的 L8 文件夹中，文件名为 bar1.html
bar.render('L8/01_柱状图.html')
print("已生成：01_柱状图.html")


# ## 8.3	绘制常用图表

# ### 8.3.1 绘制折线图

# 导入options模块和Line类

import pyecharts.options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Line
line_demo = (
    # 创建Line类的对象
    Line()
    # 添加数据
    .add_xaxis(Faker.clothes)
    .add_yaxis("商家A", [102, 132, 105, 52, 90, 111, 95], #Faker.values()
                  symbol="diamond", symbol_size=15)
    .add_yaxis("商家B", [86, 108, 128, 66, 136, 122, 105], #Faker.values()
                 symbol="triangle", symbol_size=15)
    # 设置配置项
    .set_global_opts(title_opts=opts.TitleOpts(title="折线图示例"), 
                         yaxis_opts=opts.AxisOpts(name="销售额(万元)", 
                         name_location="center", name_gap=30))
)
# 渲染图表
line_demo.render("L8/02_折线图.html")
print("已生成：02_折线图.html")


# ### 8.3.2 绘制饼图或圆环图
import pyecharts.options as opts
from pyecharts.charts import Pie
pie_demo = (
    # 创建Pie类的对象
    Pie()
    # 添加数据
    .add("", [("小米", 150), ("华为", 200), ("荣耀", 100), ("魅族", 60), 
         ("vivo", 145), ("OPPO", 160)])
    # 设置配置项
    .set_global_opts(title_opts=opts.TitleOpts(title="饼图示例"))
)
pie_demo.render("L8/03_饼图.html")
print("已生成：03_饼图.html")

#圆环图（在饼图基础上改半径）
import pyecharts.options as opts
from pyecharts.charts import Pie
pie_demo = (
    # 创建Pie类的对象
    Pie()
    # 添加数据，将内半径和外半径传入radius参数
    .add("", [("小米", 150), ("华为", 200), ("荣耀", 100), ("魅族", 60), 
         ("vivo", 145), ("OPPO", 160)], radius=[90, 160])
    # 设置配置项
    .set_global_opts(title_opts=opts.TitleOpts(title="圆环图示例"))
)
pie_demo.render("L8/04_圆环图.html")
print("已生成：04_圆环图.html")


# ### 8.3.3 绘制散点图
#传统散点图
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Scatter
scatter_demo = (
    # 创建Scatter类的对象
    Scatter()
    # 添加数据
    .add_xaxis(np.arange(1, 21).tolist())
    .add_yaxis("", np.random.randint(10, 40, 20).tolist())
    # 设置全局配置项
    .set_global_opts(title_opts=opts.TitleOpts(title="散点图示例"), 
         yaxis_opts=opts.AxisOpts(name="y轴", name_location="center", 
         name_gap=30), xaxis_opts=opts.AxisOpts(name="x轴", 
         name_location="center", name_gap=30))
)
scatter_demo.render("L8/05_散点图.html")
print("已生成：05_散点图.html")


#涟漪特效散点图（带动画）
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import EﬀectScatter
eﬀect_scatter = (
    # 创建EﬀectScatter类的对象
    EﬀectScatter()
    # 添加数据
    .add_xaxis(np.arange(1, 21).tolist())
    .add_yaxis("", np.random.randint(10, 40, 20).tolist(), symbol="pin")# 大头针样式
    # 设置全局配置项
    .set_global_opts(title_opts=opts.TitleOpts(title="涟漪特效散点图示例"), 
          yaxis_opts=opts.AxisOpts(name="y轴",name_location="center",
          name_gap=30), xaxis_opts=opts.AxisOpts(name="x轴", 
          name_location="center", name_gap=30))
)
eﬀect_scatter.render("L8/06_涟漪散点图.html")
print("已生成：06_涟漪散点图.html")

# ### 8.3.4 绘制三维柱形图

# 导入numpy库，用于生成随机数
import numpy as np
# 导入pyecharts配置项模块，简写为opts，方便设置图表样式
from pyecharts import options as opts
# 导入3D柱状图所需的Bar3D类
from pyecharts.charts import Bar3D

# 生成3D图表数据
# 格式：(x坐标, y坐标, z高度)
# i 循环 0~6（共7个：对应周一到周日）
# j 循环 0~4（共5个：对应A~E组）
# z值为 0~20 之间的随机整数
data = [(i, j, np.random.randint(0, 20)) for i in range(7) for j in range(5)]

# 链式写法创建并配置3D柱状图
bar_3d = (
    # 1. 创建3D柱状图对象
    Bar3D()

    # 2. 添加图表数据与3D坐标轴配置
    .add(
        "",  # 系列名称（这里为空）
        [[d[1], d[0], d[2]] for d in data],  # 调整数据顺序为：y, x, z
        # 设置3D-X轴：5个分组（A-E组）
        xaxis3d_opts=opts.Axis3DOpts(["A组", "B组", "C组", "D组", "E组"]),
        # 设置3D-Y轴：7个类别（周一到周日）
        yaxis3d_opts=opts.Axis3DOpts(["周一", "周二", "周三", "周四", "周五", "周六", "周日"])
    )

    # 3. 设置全局配置
    .set_global_opts(
        # 颜色映射配置：最大值设为30，用颜色深浅表示数值大小
        visualmap_opts=opts.VisualMapOpts(max_=30),
        # 设置图表标题
        title_opts=opts.TitleOpts(title="三维柱形图示例")
    )
)

# 4. 渲染输出：保存到当前目录下的 L8 文件夹中
bar_3d.render("L8/07_3D柱状图.html")
# 控制台提示：文件已生成
print("已生成：07_3D柱状图.html")

# ### 8.3.5 绘制桑基图

# 导入pyecharts配置项模块，简写为opts，用于设置图表样式
from pyecharts import options as opts
# 导入桑基图（Sankey）类，用于绘制流向/流量图
from pyecharts.charts import Sankey

# ===================== 桑基图核心：1. 定义节点（所有出现的方块） =====================
# nodes：节点列表，每个节点是一个字典，必须包含 name（节点名称）
# 桑基图中所有“方框”都要在这里先定义
nodes = [
    {"name": "消费者"},  # 起点节点
    {"name": "老客户"},  # 中间节点
    {"name": "新客户"},  # 中间节点
    {"name": "运动鞋"},  # 终点节点
    {"name": "衬衫"},  # 终点节点
    {"name": "连衣裙"},  # 终点节点
    {"name": "高跟鞋"}  # 终点节点
]

# ===================== 桑基图核心：2. 定义流向（线 + 流量大小） =====================
# links：流向列表，每个流向包含3个关键字段
# source：起点（从哪里来）
# target：终点（到哪里去）
# value：流量大小（线的粗细）
links = [
    {"source": "消费者", "target": "老客户", "value": 30},  # 消费者→老客户，流量30
    {"source": "消费者", "target": "新客户", "value": 20},  # 消费者→新客户，流量20
    {"source": "老客户", "target": "运动鞋", "value": 10},  # 老客户→运动鞋，流量10
    {"source": "老客户", "target": "衬衫", "value": 20},  # 老客户→衬衫，流量20
    {"source": "新客户", "target": "连衣裙", "value": 10},  # 新客户→连衣裙，流量10
    {"source": "新客户", "target": "高跟鞋", "value": 10}  # 新客户→高跟鞋，流量10
]

# ===================== 3. 链式写法创建桑基图 =====================
sankey_demo = (
    # 创建桑基图对象
    Sankey()

    # 添加节点、流向数据，并配置样式
    .add(
        "",  # 系列名称（为空即可，桑基图一般不用）
        nodes=nodes,  # 传入节点数据
        links=links,  # 传入流向数据

        # 线条样式配置：透明度0.2，弯曲度0.5，颜色跟随起点（source）
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),

        # 标签配置：节点名称显示在右侧
        label_opts=opts.LabelOpts(position="right")
    )

    # 设置全局配置：图表标题
    .set_global_opts(
        title_opts=opts.TitleOpts(title="桑基图示例")
    )
)

# ===================== 4. 渲染保存 =====================
# 保存为HTML文件到当前目录
sankey_demo.render("L8/08_桑基图.html")
# 控制台输出提示
print("已生成：08_桑基图.html")


# ## 8.4	绘制组合图表
# ### 8.4.1 并行多图

import pyecharts.options as opts
from pyecharts.charts import Bar, Line, Grid
x_data = ["小米", "荣耀", "华为", "中兴", "魅族", 'vivo', 'OPPO'] 
y_a = [107, 36, 102, 91, 51, 113, 45] 
y_b = [104, 60, 33, 138, 105, 111, 91]
bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("商家A", y_a)
    .add_yaxis("商家B", y_b)
    .set_global_opts(title_opts=opts.TitleOpts(title="组合图表-柱形图", pos_left="0%"),
           yaxis_opts=opts.AxisOpts(name="销售额(万元)",
           name_location="center", name_gap=30))
)
line = (Line()
    .add_xaxis(x_data)
    .add_yaxis("商家A", y_a, label_opts=opts.LabelOpts(position='bottom'))
    .add_yaxis("商家B", y_b)
    .set_global_opts(title_opts=opts.TitleOpts(title="组合图表-折线图",
          pos_left="0%", pos_top="48%"), legend_opts=opts.LegendOpts(pos_top="48%"),
          yaxis_opts=opts.AxisOpts(name="销售额(万元)",
          name_location="center", name_gap=30))
)

grid = (
    # 创建Grid类的对象，生成并行多图形式的组合图表
    Grid()
    # 添加图表对象和配置项
    .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
    .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
)

grid.render("L8/10_并行多图.html")
print("已生成：10_并行多图.html")


# ### 8.4.2 顺序多图

# 导入pyecharts配置项模块，简写为opts
from pyecharts import options as opts
# 导入柱状图、折线图、顺序多图Page类
from pyecharts.charts import Bar, Line, Page

# ---------------------- 1. 准备图表数据 ----------------------
# X轴：手机品牌名称
x_data = ["小米", "荣耀", "华为", "中兴", "魅族", "vivo", "OPPO"]
# 商家A的销售额数据
y_a = [107, 36, 102, 91, 51, 113, 45]
# 商家B的销售额数据
y_b = [104, 60, 33, 138, 105, 111, 91]

# ---------------------- 2. 创建第一个图表：柱状图 ----------------------
bar = (
    Bar()  # 创建柱状图对象
    .add_xaxis(x_data)  # 添加X轴数据
    .add_yaxis("商家A", y_a)  # 添加Y轴数据：商家A
    .add_yaxis("商家B", y_b)  # 添加Y轴数据：商家B
    .set_global_opts(
        # 设置标题，并且标题靠左对齐
        title_opts=opts.TitleOpts(title="组合图表-柱形图", pos_left="0%"),
        # 设置Y轴名称、位置、间距
        yaxis_opts=opts.AxisOpts(name="销售额(万元)", name_location="center", name_gap=30)
    )
)

# ---------------------- 3. 创建第二个图表：折线图 ----------------------
line = (
    Line()  # 创建折线图对象
    .add_xaxis(x_data)  # 添加X轴数据
    .add_yaxis("商家A", y_a)  # 添加Y轴数据：商家A
    .add_yaxis("商家B", y_b)  # 添加Y轴数据：商家B
    .set_global_opts(
        # 设置标题，并且标题靠左对齐
        title_opts=opts.TitleOpts(title="组合图表-折线图", pos_left="0%"),
        # 设置Y轴名称、位置、间距
        yaxis_opts=opts.AxisOpts(name="销售额(万元)", name_location="center", name_gap=30)
    )
)

# ---------------------- 4. 使用 Page 实现【顺序多图】 ----------------------
# Page：把多个图表按 从上到下顺序 放在同一个网页里展示
# page_title：设置网页标题
# interval：图表之间的间距
page = Page(page_title="顺序多图", interval=2)

# 把柱状图、折线图依次添加到page中
page.add(bar, line)

# ---------------------- 5. 渲染并保存到 L8 文件夹 ----------------------
page.render('L8/11_顺序多图.html')
print("已生成：11_顺序多图.html")


# ### 8.4.3 选项卡多图

from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Tab
x_data = ["小米", "荣耀", "华为", "中兴", "魅族", "vivo", "OPPO"] 
y_a = [107, 36, 102, 91, 51, 113, 45] 
y_b = [104, 60, 33, 138, 105, 111, 91]
bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("商家A", y_a)
    .add_yaxis("商家B", y_b)
    .set_global_opts(yaxis_opts=opts.AxisOpts(name="销售额(万元)", 
                         name_location="center", name_gap=30))
)
line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis("商家A", y_a)
    .add_yaxis("商家B", y_b)
    .set_global_opts(yaxis_opts=opts.AxisOpts(name="销售额(万元)", 
                        name_location="center", name_gap=30))
)


# 创建选项卡多图（Tab）
# Tab：实现“选项卡切换”效果，点不同标签显示不同图表
tab = Tab()
# 给选项卡添加图表：add(图表对象, 选项卡显示文字)
tab.add(bar, "柱形图")    # 第一个标签：柱形图
tab.add(line, "折线图")   # 第二个标签：折线图


tab.render('L8/12_选项卡多图.html')
print("已生成：12_选项卡多图.html")


# ### 8.4.4 时间线轮播多图
# 导入pyecharts内置测试数据 Faker
from pyecharts.faker import Faker
# 导入配置项模块，简写为opts
from pyecharts import options as opts
# 导入柱状图、时间线轮播图 Timeline 类
from pyecharts.charts import Bar, Timeline

# ---------------------- 1. 创建时间线轮播图对象 ----------------------
# Timeline：按“时间节点”自动/手动切换图表，适合动态展示趋势
tl = Timeline()

# ---------------------- 2. 循环生成 2020~2024 年的图表 ----------------------
for year in range(2020, 2025):  # 循环 2020、2021、2022、2023、2024 共5年
    # 每年创建一个独立的柱状图
    bar = (
        Bar()  # 创建柱状图
        .add_xaxis(Faker.clothes)  # X轴使用Faker内置的服装数据
        # Y轴使用Faker随机生成的数值，系列名称为空
        .add_yaxis("", Faker.values())
        # 设置全局配置：Y轴名称、居中、间距
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="销售额(万元)",
                name_location="center",
                name_gap=30
            ),
            # 标题靠左 + 显示当前年份（更清晰）
            title_opts=opts.TitleOpts(title=f"{year}年商品销量", pos_left="0%")
        )
    )

    # ---------------------- 3. 配置时间线样式（只需设置一次） ----------------------
    # symbol：时间节点样式 → diamond 菱形
    # symbol_size：节点大小
    # is_auto_play：是否自动播放
    tl.add_schema(symbol="diamond", symbol_size=15, is_auto_play=True)

    # ---------------------- 4. 把当前年份的图表加入时间线 ----------------------
    # tl.add(图表对象, 时间点文字)
    tl.add(bar, "{}年".format(year))

# ---------------------- 5. 渲染保存到 L8 文件夹 ----------------------
tl.render("L8/13_时间线轮播多图.html")
print("已生成：13_时间线轮播多图.html")

# ## 8.5	定制图表主题

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
x_data = ["小米", "荣耀", "华为", "中兴", "魅族", 'vivo', 'OPPO'] 
y_a = [107, 36, 102, 91, 51, 113, 45] 
y_b = [104, 60, 33, 138, 105, 111, 91]
bar = (
    # 创建Bar类的对象，修改图表的主题
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))#主题设置
    .add_xaxis(x_data)
    .add_yaxis("商家A", y_a)   
    .add_yaxis("商家B", y_b)
    .set_global_opts(title_opts=opts.TitleOpts(title="柱形图-ROMA主题"),
                        yaxis_opts=opts.AxisOpts(name="销售额(万元)",
                        name_location="center", name_gap=30))
)
bar.render("L8/14_主题图表.html")
print("已生成：14_主题图表.html")


# ## 8.6	整合Web框架


# ## 8.7	实战演练：虎扑社区分析
# #### 1.	画图分析虎扑社区各板块发帖数
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Pie, Line, Page 
pie_hupu = (
    # 创建Pie类的对象
    Pie()
    # 添加数据
    .add("", [('NBA', 232345), ('CBA', 16976), ('国际足球', 44381), 
                ('中国足球', 124), ('步行街', 512266), ('游戏电竞', 129065), 
                ('自建板块', 3805), ('运动装备', 35124), ('综合体育', 4454), 
                ('虎扑社团', 646), ('站务管理', 34467)], 
                center=["50%", "50%"], radius=[100, 160])
    # 设置全局配置项
    .set_global_opts(title_opts=opts.TitleOpts(title="虎扑社区各板块发帖数"), 
                        legend_opts=opts.LegendOpts(pos_left=10, 
                        pos_top=80, orient='vertical'))
)

# 创建Page类的对象
page1 = Page()
# 添加图表对象
page1.add(pie_hupu)
# 渲染图表
page1.render('L8/虎扑社区1.html')


# #### 2.	画图分析虎扑社区和NBA板块24小时的发帖量

line_hupu = (
    # 创建Line类的对象，修改图表主题
    Line(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
    .add_xaxis(['{} : 00'.format(num) for num in range(24) if num%2==0])
    .add_yaxis('NBA', [259, 114, 134, 397, 840, 1577, 1413, 713, 
            647, 448, 462, 514], symbol='diamond', symbol_size=15)
    .add_yaxis('虎扑', [1221, 370, 359, 845, 2270, 3582, 2947, 2215, 
            2106, 1843, 2045, 2178], symbol='triangle', symbol_size=15)
    .set_global_opts(title_opts=opts.TitleOpts(
          title="虎扑社区和NBA板块24小时发帖数"),
          yaxis_opts=opts.AxisOpts(name="发帖数(个)", 
          name_location="center", name_gap=40))
)


page2 = Page()
# 添加图表对象
page2.add(pie_hupu, line_hupu)
# 渲染图表
page2.render('L8/虎扑社区2.html')