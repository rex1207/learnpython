import pandas as pd
df = pd.read_excel('zz800.xls', keep_default_na=False)
# 重设列名
df.columns = ['code', 'name', 'peg1', 'peg2', 'peg3', 'pe1', 'pe2', 'pe3',
              'annual_yield', 'vs_hs300_this_year', 'vs_hs300_1_year',
              'record_high', 'record_low', 'stage_high', 'stage_low',
              'ma_250', 'current_price', 'debt_to_assets_ratio', 'roe',
              'goodwill', 'net_asset', 'rating_count', 'impawn_rate']
print(df)
# 将str的列转换为数值类型
df = df.apply(pd.to_numeric, errors='ignore')
# df = df.fillna(value={'goodwill': 0, 'rating_count': 0})
# 替换某些列异常数据为0
df = df.replace({'goodwill': '——', 'rating_count': '——', 'impawn_rate': '——'}, 0)
# 替换某些列异常数据为9999
df = df.replace({'peg1': '——', 'peg2': '——', 'peg3': '——'}, 9999)
df = df.replace({'pe1': '——', 'pe2': '——', 'pe3': '——'}, 9999)
print(df)
print(df.dtypes)
df = df[df['debt_to_assets_ratio'] > 0.2]
df['goodwill_net_asset_ratio'] = \
    df[['goodwill', 'net_asset']].apply(lambda x: float(x["goodwill"])/float(x["net_asset"]), axis=1)
df['ma_250_ratio'] = \
    df[['ma_250', 'current_price']].apply(lambda x: float(x["current_price"])/float(x["ma_250"]), axis=1)
print(df)
# 股价高于年线2倍的
print(df.loc[df['ma_250_ratio'] > 2])
# 股价高于年线的
print(df.loc[df['ma_250_ratio'] > 1])
# 商誉高于20%的
print(df.loc[df['goodwill_net_asset_ratio'] > 0.2])
# ROE高于10&年化收益率高于10%的
candidate = df[(df['roe'] > 10)
         & (df['annual_yield'] > 10)
         & (df['annual_yield'] < 50)
         & (df['stage_high'] == '是')
         & (df['peg2'] < 1.5)
         & (df['peg3'] < 1.2)
         & (df['pe2'] < 50)
         & (df['pe3'] < 30)
         & (df['goodwill_net_asset_ratio'] < 0.2)
         & (df['impawn_rate'] < 20)
         & (df['rating_count'] > 0)
         & (df['ma_250_ratio'] > 1)
         & (df['ma_250_ratio'] < 1.5)]
print(candidate)
print(candidate.to_dict('records'))
# stocks = []
# hot_stocks = []
# for index, row in df.iterrows():
#     # print(row) # 输出每行
#     stock = {'code': row['code'], 'name': row['name'],
#              'peg1': row['peg1'], 'peg2': row['peg2'], 'peg3': row['peg3'],
#              'pe1': row['pe1'], 'pe2': row['pe2'], 'pe3': row['pe3'],
#              'annual_yield': row['annual_yield'],
#              'vs_hs300_this_year': row['vs_hs300_this_year'],
#              'vs_hs300_1_year': row['vs_hs300_1_year'],
#              'record_high': row['record_high'], 'record_low': row['record_low'],
#              'stage_high': row['stage_high'], 'stage_low': row['stage_low'],
#              'ma_250': row['ma_250'], 'current_price': row['current_price'],
#              'debt_to_assets_ratio': row['debt_to_assets_ratio'],
#              'roe': row['roe'], 'rating_count': row['rating_count'],
#              'goodwill': row['goodwill'],
#              'net_asset': row['net_asset']}
#     if (isinstance(stock['goodwill'], float) or isinstance(stock['goodwill'], int))\
#             and (isinstance(stock['net_asset'], float) or isinstance(stock['net_asset'], int)):
#         goodwill = float(stock['goodwill'])
#         net_asset = float(stock['net_asset'])
#         stock.update({'goodwill_net_asset_ratio': goodwill/net_asset})
#     if (isinstance(stock['ma_250'], float) or isinstance(stock['ma_250'], int)) \
#             and (isinstance(stock['current_price'], float) or isinstance(stock['current_price'], int)):
#         stock.update({'ma_250_ratio': float(stock['current_price'])/float(stock['ma_250'])})
#         # 股价高于年线2倍的
#         if stock['ma_250_ratio'] > 2:
#             hot_stocks.append(stock)
#     if stock['name']:
#         stocks.append(stock)
# print(stocks)
# print(len(stocks))
# print(hot_stocks)
# print(len(hot_stocks))
# df = pd.DataFrame(stocks)
# print(df)
# df.to_excel("output.xlsx", index=False)
