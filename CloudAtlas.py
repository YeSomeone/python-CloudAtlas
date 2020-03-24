#1.导入所需库和模块
import requests
import json
import wordcloud #第三方词云模块
import matplotlib.pyplot as plt #显示词云图形的模块

#2.请求数据
url = 'https://api.yimian.xyz/coro'
data = requests.get(url).text

#3.解析数据——转换为JSON对象
city_dict = {}
json_data = json.loads(data)
for p in json_data:
    if 'cities' in p:
        for c in p['cities']:
            cityName = c['cityName']
            cCount = c['confirmedCount']
            sCount = c['suspectedCount']
            total = int(cCount) + int(sCount)
            city_dict[cityName] = total
    else:
        cityname = p['provinceName']
        cCount = p['confirmedCount']
        sCount = p['suspectedCount']
        total = int(cCount) + int(sCount)
        city_dict[cityName] = total

#4.写入文件
with open('ncov.txt','w') as n:
    for k, v in city_dict.items():
        n.write(f"{k}:{v}\n")

#5.获得生成词云所需数据
ccloud = wordcloud.WordCloud(background_color='white', width=1600, height=800, font_path='D:\code\simkai.ttf') #设置词云图片的背景大小以及字体
ccloud.generate_from_frequencies(frequencies=city_dict) #指定数据来源并生成词云所需要的数据

#6.将数据转化为词云图形并显示
plt.figure()
plt.imshow(ccloud, interpolation='bilinear')
plt.axis('off') #关闭显示坐标
plt.show()