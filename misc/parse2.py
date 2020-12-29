import requests
import json
import matplotlib.pyplot as plt


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

    # 中文乱码
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    # fig, ax = plt.subplots(figsize=(100, 100))
    fig, ax = plt.subplots()
    # plt.gca().tick_params(axis='y', labelcolor='red')
    y_labels = ax.get_yticklabels()
    print(len(y_labels))
    print(len(ax.get_yticklabels()))
    for label in y_labels:
        print(label)
    y_labels[-1].set_color('red')
    ax.barh(x, y)
    # ax.bar(x, y)
    # for a, b in zip(x, y):
    #     plt.text(a, b - 0.3, '%.3f' % b, ha='center', va='bottom', fontsize=15)
    plt.xticks(rotation=90)
    plt.show()



