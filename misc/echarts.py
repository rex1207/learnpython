import requests
import json
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Bar

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


if __name__ == '__main__':
    # vote_list = [1040, 1046, 1054]
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
    data_list.sort(key=lambda v: v['vote'], reverse=True)
    # print(data_list)
    value = {}
    count = 1
    for data in data_list:
        # print(data)
        key = '编号'+str(data['sort_num'])+":"+data['title']+'(排名'+str(count)+')'
        value[key] = data['vote']
        count += 1
    print(value)

    x = list(value.keys())
    y = list(value.values())

    c = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("商家A", y)
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-翻转 XY 轴"))
            .render("bar_reversal_axis.html")
    )



