import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import requests
import json, collections

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

# fig = go.Figure(
#     data=[go.Bar(x=[2, 1, 3], y=['a','b','c'], orientation='h')],
#     layout_title_text="Native Plotly rendering in Dash"
# )

fig = go.Figure(
    data=[go.Bar(x=y, y=x, orientation='h')],
    layout_title_text="Native Plotly rendering in Dash"
)

app = dash.Dash(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig),
])


if __name__ == "__main__":
    app.run_server(debug=True)
