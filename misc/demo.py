""" Shows how to use flask and matplotlib together.
Shows SVG, and png.
The SVG is easier to style with CSS, and hook JS events to in browser.
python3 -m venv venv
. ./venv/bin/activate
pip install flask matplotlib
python flask_matplotlib.py
"""
import io
import random
from flask import Flask, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
import requests
import json
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import collections

app = Flask(__name__)


def get_vote(vote_id=1040):
    headers = {'content-type': 'application/json',
               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'}
    # r = requests.get('https://activity.wifiwx.com/vote/minxin/rwabout.html?ids=1040&id=69', headers=headers)
    r = requests.get('https://activity.wifiwx.com/api/vote/vote_info?id=69&ids='+str(vote_id), headers=headers)
    response = r.text
    # print(r.text)
    d = json.loads(response)
    data = d.get('data')
    # print(data)
    return data

@app.route("/")
def index():
    """ Returns html with the img tag for your plot.
    """
    num_x_points = int(request.args.get("num_x_points", 50))
    # in a real app you probably want to use a flask template.
    return f"""
    <h1>Flask and matplotlib</h1>
    <h2>Random data with num_x_points={num_x_points}</h2>
    <form method=get action="/">
    </form>
    <h3>Plot as a SVG</h3>
    <img src="/matplot-as-image-{num_x_points}.png"
         alt="random points as png"
         height="500"
    >
    <img src="/matplot-as-image-{num_x_points}.svg"
         alt="random points as svg"
         height="500"
    >
    """
    # from flask import render_template
    # return render_template("yourtemplate.html", num_x_points=num_x_points)


@app.route("/matplot-as-image-<int:num_x_points>.png")
def plot_png(num_x_points=50):
    """ renders the plot on the fly.
    """
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(num_x_points)
    axis.plot(x_points, [random.randint(1, 30) for x in x_points])

    vote_list = list(range(1032, 1072))
    # vote_list.append(1068)
    # vote_list.append(1069)
    data_list = []
    for vote in vote_list:
        data = get_vote(vote)
        if data and data['desc']:
            data_list.append(data)
    print(len(data_list))
    # data_list.sort(key=lambda v: v['sort_num'])
    # 按票数排序
    data_list.sort(key=lambda v: v['vote'], reverse=False)
    # print(data_list)
    # value = {}
    value = collections.OrderedDict()
    count = 25
    num_10 = 0  # 第10名票数
    for data in data_list:
        # print(data)
        key = '编号' + str(data['sort_num']) + ":" + data['title'] + '(排名' + str(count) + ')'
        value[key] = data['vote']
        count -= 1
        if count == 9:
            num_10 = data['vote']
            print('num 10:', num_10)
    print(value)

    x = list(value.keys())
    y = list(value.values())

    # 解决中文乱码
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    fig, ax = plt.subplots()

    # 横向柱状图
    ax.barh(x, y)
    c = 0
    diff = 5000
    gap = 0.3
    for a, b in zip(x, y):
        print(a, b)
        # 显示柱状图上数字
        if "排名10" in a:
            plt.text(diff, c - gap, b, bbox=dict(facecolor='red', alpha=0.5))
        elif '编号3' in a or '编号6' in a:
            print(num_10, b)
            msg = '距离第10名还差' + str(num_10 - b)
            plt.text(diff, c - gap, str(b) + msg, bbox=dict(facecolor='red', alpha=0.5))
        else:
            plt.text(diff, c - gap, b, ha='center', va='bottom', fontsize=8)
        c += 1
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output, bbox_inches = 'tight')
    return Response(output.getvalue(), mimetype="image/png")


# @app.route("/matplot-as-image-<int:num_x_points>.svg")
# def plot_svg(num_x_points=50):
#     """ renders the plot on the fly.
#     """
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     x_points = range(num_x_points)
#     axis.plot(x_points, [random.randint(1, 30) for x in x_points])
#
#     output = io.BytesIO()
#     FigureCanvasSVG(fig).print_svg(output)
#     return Response(output.getvalue(), mimetype="image/svg+xml")


@app.route("/matplot-as-image-<int:num_x_points>.svg")
def plot_svg(num_x_points=50):
    """ renders the plot on the fly.
    """
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(num_x_points)
    axis.plot(x_points, [random.randint(1, 30) for x in x_points])

    vote_list = list(range(1032, 1072))
    # vote_list.append(1068)
    # vote_list.append(1069)
    data_list = []
    for vote in vote_list:
        data = get_vote(vote)
        if data and data['desc']:
            data_list.append(data)
    print(len(data_list))
    # data_list.sort(key=lambda v: v['sort_num'])
    # 按票数排序
    data_list.sort(key=lambda v: v['vote'], reverse=False)
    # print(data_list)
    # value = {}
    value = collections.OrderedDict()
    count = 25
    num_10 = 0  # 第10名票数
    for data in data_list:
        # print(data)
        key = '编号' + str(data['sort_num']) + ":" + data['title'] + '(排名' + str(count) + ')'
        value[key] = data['vote']
        count -= 1
        if count == 9:
            num_10 = data['vote']
            print('num 10:', num_10)
    print(value)

    x = list(value.keys())
    y = list(value.values())

    # 解决中文乱码
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    fig, ax = plt.subplots()

    # 横向柱状图
    ax.barh(x, y)
    c = 0
    diff = 5000
    gap = 0.3
    for a, b in zip(x, y):
        print(a, b)
        # 显示柱状图上数字
        if "排名10" in a:
            plt.text(diff, c - gap, b, bbox=dict(facecolor='red', alpha=0.5))
        elif '编号3' in a or '编号6' in a:
            print(num_10, b)
            msg = '距离第10名还差' + str(num_10 - b)
            plt.text(diff, c - gap, str(b) + msg, bbox=dict(facecolor='red', alpha=0.5))
        else:
            plt.text(diff, c - gap, b, ha='center', va='bottom', fontsize=8)
        c += 1
    # plt.show()

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output,bbox_inches = 'tight')
    return Response(output.getvalue(), mimetype="image/svg+xml")


if __name__ == "__main__":
    import webbrowser

    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)
