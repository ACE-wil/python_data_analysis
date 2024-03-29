from random import randrange
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

from flask.json import jsonify
from flask import Flask, render_template, request
from markupsafe import Markup
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.charts import Bar
from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.faker import Faker
from pyecharts.globals import CurrentConfig
import pandas
from requests_html import HTMLSession
import json
import pandas as pd

#%%
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))
app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

def get_data(job_name,city_name):
    import pandas
    from requests_html import HTMLSession
    import json
    import pandas as pd
    import requests
    用户输入职位 = job_name
    用户输入城市 = city_name
    城市编码 = {
    '北京':'010',
    '上海':'020',
    '广州':'050020',
    '深圳':'050090',

}
    url = "https://apic.liepin.com/api/com.liepin.searchfront4c.pc-search-job"
    payload = {
    "data": {
        "mainSearchPcConditionForm": {
            "city": 城市编码[用户输入城市],
            "dq": 城市编码[用户输入城市],
            "pubTime": "",
            "currentPage": 0,
            "pageSize": 40,
            "key": str(用户输入职位),
            "suggestTag": "",
            "workYearCode": "0",
            "compId": "",
            "compName": "",
            "compTag": "",
            "industry": "",
            "salary": "",
            "jobKind": "",
            "compScale": "",
            "compKind": "",
            "compStage": "",
            "eduLevel": ""
        },
        "passThroughForm": {
            "scene": "input",
            "skId": "",
            "fkId": "",
            "ckId": "h2c8pxojavrmo1w785z7ueih2ybfpux8",
            "suggest": None
        }
    }
}
    session = HTMLSession()
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "399",
    "Content-Type": "application/json;charset=UTF-8;",
    "Cookie": "inited_user=0b40e95258783b742e53b3c4507c0e74; __gc_id=ba575649f262440b97583f40312082aa; __uuid=1680367209983.58; _ga=GA1.1.1780140015.1681902728; need_bind_tel=false; new_user=false; c_flag=fd8e161021d62dd50e5032f3c60a147a; imClientId=40be7e37d455d9dca12bac537377bfad; imId=40be7e37d455d9dc3e4f5f0f695234e5; imClientId_0=40be7e37d455d9dca12bac537377bfad; imId_0=40be7e37d455d9dc3e4f5f0f695234e5; __tlog=1687614466064.74%7C00000000%7C00000000%7Cs_00_t00%7Cs_00_t00; XSRF-TOKEN=AxC3zYUoTCa4UE6UMEBu3Q; acw_tc=276077df16876149605383539e9698e9728a5073c698641df54fd5db7119a7; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1686135762,1687265958,1687443970,1687614959; UniqueKey=fe87a9f3258ac642a9dba665e9526a14; liepin_login_valid=0; lt_auth=6eZeOHQMxlXw4XfcjTcLtacfj9%2BsU2yYpnhehk8FhoK5W6Ll4P%2FgSwuCq7gH%2FioIqxJ2Jv8zMLb2Mu7%2FzXpD7ksa8FGnlZ6utf6k1XweTuZiHuyflMXuqsjQQ5wtrXo6ykpgn2si0HU%3D; access_system=C; user_roles=0; user_photo=5f8fa3a679c7cc70efbf444e08u.png; user_name=%E6%B2%88%E8%BF%9E%E6%9D%B0; inited_user=0b40e95258783b742e53b3c4507c0e74; imApp_0=1; __session_seq=6; __uv_seq=13; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1687614997; fe_im_socketSequence_new_0=2_2_2; fe_im_opened_pages=; fe_im_connectJson_0=%7B%220_fe87a9f3258ac642a9dba665e9526a14%22%3A%7B%22socketConnect%22%3A%222%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D; _ga_54YTJKWN86=GS1.1.1687614958.17.1.1687615020.0.0.0",
    "Host": "api-c.liepin.com",
    "Origin": "https://www.liepin.com",
    "Referer": "https://www.liepin.com/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "X-Client-Type": "web",
    "X-Fscp-Bi-Stat": "{\"location\": \"https://www.liepin.com/zhaopin/?inputFrom=head_navigation&scene=init&workYearCode=1&ckId=oce2zl0xqfy64oyvrvccr557wnfp6j6a\"}",
    "X-Fscp-Fe-Version": "",
    "X-Fscp-Std-Info": "{\"client_id\": \"40108\"}",
    "X-Fscp-Trace-Id": "5f4fbbc3-01f7-44e5-82b2-fb737d5d07e0",
    "X-Fscp-Version": "1.1",
    "X-Requested-With": "XMLHttpRequest",
    "X-Xsrf-Token": "AxC3zYUoTCa4UE6UMEBu3Q"
}
    r = session.post(url, data=json.dumps(payload), headers=headers)
    response_data = r.json()
    page = response_data['data']['pagination']['totalPage']
    response_df = []
    for i in range(page): # 需要判断页面的数据有多少页
        payload['data']['mainSearchPcConditionForm']['currentPage']=i
        # send a POST request with headers
        r = requests.post(url, data=json.dumps(payload), headers=headers)
    response_data = r.json()
    print(response_data)
    df = pd.json_normalize(response_data['data']['data']['jobCardList'])
    response_df.append(df)
    df = pd.concat(response_df)
    key = payload['data']['mainSearchPcConditionForm']['key']
    df.to_excel('liepin2.xlsx')
    df = pd.read_excel('liepin2.xlsx')
    df

    df_PM_gz =  df[['job.labels','job.refreshTime','job.title','job.salary','job.dq','job.topJob','job.requireWorkYears','job.requireEduLevel','comp.compStage','comp.compName','comp.compIndustry','comp.compScale']]
    df_PM_gz

    df_PM_gz['job.dq'].value_counts()
    地区 = [ df_PM_gz['job.dq'].value_counts().index.tolist()[i].split('-')[1]\
             for i,v in enumerate(df_PM_gz['job.dq'].value_counts().index.tolist()) if '-' in v]
    地区
    岗位个数 = [ df_PM_gz['job.dq'].value_counts().values.tolist()[i] for i,v in enumerate(df_PM_gz['job.dq'].value_counts().index.tolist()) if "-" in v]
    岗位个数
    df_PM_gz['job.title'][df_PM_gz['job.title'].str.contains('（')].str.split('（').apply(lambda x: x[0])
    df_job_title = df_PM_gz['job.title'].apply(lambda x: x.split('（')[0].split('/')[0].split('(')[0]).value_counts()
    df_job_title.index.tolist()
    len(df_job_title.index.tolist())
    df_job_title.values.tolist()
    df_PM_gz['job.title'].value_counts()
    PM_title_words = [(df_job_title.index.tolist()[i], df_job_title.values.tolist()[i]) for i in
                      range(1, len(df_job_title.index.tolist()))]
    PM_title_words
    df_PM_gz['job.labels']
    df_PM_gz['job.labels'].values
    df_PM_gz['job.labels'].apply(lambda x: eval(x)).tolist()
    PM_labels_list = [j for i in df_PM_gz['job.labels'].apply(lambda x: eval(x)).tolist() for j in i]
    PM_labels_list
    PM_labels_words = [(i, PM_labels_list.count(i)) for i in set(PM_labels_list)]
    PM_labels_words
    df_PM_gz = df_PM_gz.rename(columns={
        'job.labels': '职位标签',
        'job.refreshTime': '职位更新时间',
        'job.title': '职位',
        'job.salary': '薪资',
        'job.dq': '地区',
        'job.topJob': '是否top职位',
        'job.requireWorkYears': '工作年限',
        'job.requireEduLevel': '学历',
        'comp.compStage': '公司融资情况',
        'comp.compName': '公司名称',
        'comp.compIndustry': '行业',
        'comp.compScale': '规模'
    })
    df_PM_gz
    非薪资面议 = df_PM_gz[~df_PM_gz['薪资'].str.contains("面议|元/天")]
    非薪资面议
    非薪资面议_detail = 非薪资面议['薪资'].apply(lambda x: x.split('薪')[0].split('·')).tolist()
    非薪资面议_detail
    平均薪资 = [(int(i[0].split('-')[0]) + int(i[0].split('-')[1].split('k')[0])) / 2 \
                    if len(i) == 1 else round(
        (int(i[0].split('-')[0]) + int(i[0].split('-')[1].split('k')[0])) / 2 * int(i[1]) / 12, 1) \
                for i in 非薪资面议_detail]
    平均薪资
    非薪资面议['平均薪资'] = 平均薪资
    分地区_平均薪资 = 非薪资面议.groupby('地区').agg({'平均薪资': 'median'})
    分地区_平均薪资_values = [round(i[0], 1) for i in 分地区_平均薪资.values.tolist()]
    分地区_平均薪资_values
    分地区_平均薪资_index = 分地区_平均薪资.index.tolist()
    分地区_平均薪资_index

    return 地区,岗位个数,PM_title_words,分地区_平均薪资_index,分地区_平均薪资_values


from pyecharts.charts import Map
def map_chart(地区,岗位个数) -> Map:
    import time
    time.localtime()
    output_time = str(time.localtime().tm_year) + '-' \
                  + str(time.localtime().tm_mon) + '-' \
                  + str(time.localtime().tm_mday) + '_' \
                  + str(time.localtime().tm_hour) + ':' \
                  + str(time.localtime().tm_min)
    output_time
    city_name = request.form.get('city_name')
    job_name = request.form.get('job_name')

    c = (
        Map()
        .add(city_name, [list(z) for z in zip(地区, 岗位个数)], city_name)
        .set_global_opts(
            title_opts=opts.TitleOpts(title=city_name+job_name+"岗位地区分布"+"数据获取时间:"+output_time), visualmap_opts=opts.VisualMapOpts()
        )
    )
    return c

def word_chart(PM_title_words)->WordCloud():
    import time
    time.localtime()
    output_time = str(time.localtime().tm_year) + '-' \
                  + str(time.localtime().tm_mon) + '-' \
                  + str(time.localtime().tm_mday) + '_' \
                  + str(time.localtime().tm_hour) + ':' \
                  + str(time.localtime().tm_min)
    output_time
    job_name = request.form.get('job_name')
    city_name = request.form.get('city_name')
    d = (
        WordCloud()
        .add("", PM_title_words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
        .set_global_opts(title_opts=opts.TitleOpts(title=city_name+job_name + "热门岗位词云图/"+"数据获取时间："+output_time))
    )
    return d

def mid_chart(分地区_平均薪资_index,分地区_平均薪资_values)->WordCloud():
    import time
    time.localtime()
    output_time = str(time.localtime().tm_year) + '-' \
                  + str(time.localtime().tm_mon) + '-' \
                  + str(time.localtime().tm_mday) + '_' \
                  + str(time.localtime().tm_hour) + ':' \
                  + str(time.localtime().tm_min)
    output_time
    job_name = request.form.get('job_name')
    city_name = request.form.get('city_name')
    my_string = '                                      '
    h = (
        Bar()
        .add_xaxis([i.split('-')[1] for i in 分地区_平均薪资_index[1:]])
        .add_yaxis("地区", 分地区_平均薪资_values[1:])
        .set_global_opts(
            title_opts=opts.TitleOpts(title=city_name+job_name+"各地区平均薪资"+"单位:k"+my_string+"数据获取时间:"+output_time),
            brush_opts=opts.BrushOpts(),
        )

    )
    return h

@app.route("/")
def index_boot():
    return render_template("index_bootstrap.html")



@app.route('/word', methods=['POST'])

def word():
    job_name = request.form.get('job_name')
    city_name = request.form.get('city_name')
    from markupsafe import Markup
    _, _, PM_title_words,_, _,= get_data(job_name, city_name)
    d = word_chart(PM_title_words)
    return Markup(d.render_embed())

@app.route('/map', methods=['POST'])
def map():
    job_name = request.form.get('job_name')
    city_name = request.form.get('city_name')
    from markupsafe import Markup
    地区, 岗位个数,_,_, _, = get_data(job_name, city_name)
    print(地区, 岗位个数)
    f = map_chart(地区, 岗位个数)
    return Markup(f.render_embed())


@app.route('/mid', methods=['POST'])
def mid():
    job_name = request.form.get('job_name')
    city_name = request.form.get('city_name')
    from markupsafe import Markup
    _,_, _, 分地区_平均薪资_index,分地区_平均薪资_values= get_data(job_name, city_name)
    g = mid_chart(分地区_平均薪资_index,分地区_平均薪资_values)
    return Markup(g.render_embed())
#@app.route('/index')
#def index():
 #   from markupsafe import Markup
 #   地区,岗位个数 = get_data("产品经理", "广州")
  #  print(地区,岗位个数)
 #   c = map_chart(地区, 岗位个数)
 #   return Markup(c.render_embed())



# @app.route("/mapchart")
# def indexxx():
#     c = map_chart()
#     return c.dump_options_with_quotes()

@app.route("/tubiao")
def tubiao():
   return render_template("tubiao.html")


# idx = 9


# @app.route("/lineDynamicData")
# def update_line_data():
#     global idx
#     idx = idx + 1
#     return jsonify({"name": idx, "value": randrange(50, 80)})


if __name__ == "__main__":
    app.run()