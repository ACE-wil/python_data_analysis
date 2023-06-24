
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
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '412',
    'Content-Type': 'application/json;charset=UTF-8;',
    'Cookie': 'inited_user=0b40e95258783b742e53b3c4507c0e74; __gc_id=ba575649f262440b97583f40312082aa; __uuid=1680367209983.58; _ga=GA1.1.1780140015.1681902728; need_bind_tel=false; new_user=false; c_flag=fd8e161021d62dd50e5032f3c60a147a; imClientId=40be7e37d455d9dca12bac537377bfad; imId=40be7e37d455d9dc3e4f5f0f695234e5; imClientId_0=40be7e37d455d9dca12bac537377bfad; imId_0=40be7e37d455d9dc3e4f5f0f695234e5; XSRF-TOKEN=p9QLPjJMQx-fu-i4zHjHkA; __tlog=1686135762104.38%7C00000000%7C00000000%7Cs_o_007%7Cs_o_007; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1683716818,1685532618,1685585264,1686135762; acw_tc=2760828a16861357626407991edc7db7268d07d91730c11cbe4406bd01776f; UniqueKey=fe87a9f3258ac642a9dba665e9526a14; liepin_login_valid=0; lt_auth=s7sPPHQMxlXw4XfcjTcLtacfj9%2BsU2yYpnhehk8FhoK5W6Ll4P%2FgSwuCq7gH%2FioIqx0mJf0zMLb2M%2Bn9zHtK6EMS%2BVGnlZ6utf6k0HsCUeZkJsW2vezHg%2FXUQp0lnEAA8nJbpEIL%2BVzO; access_system=C; user_roles=0; user_photo=5f8fa3a679c7cc70efbf444e08u.png; user_name=%E6%B2%88%E8%BF%9E%E6%9D%B0; inited_user=0b40e95258783b742e53b3c4507c0e74; imApp_0=1; fe_im_socketSequence_new_0=2_1_2; fe_im_connectJson_0=%7B%220_fe87a9f3258ac642a9dba665e9526a14%22%3A%7B%22socketConnect%22%3A%223%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D; fe_im_opened_pages=; _ga_54YTJKWN86=GS1.1.1686135760.13.1.1686135955.0.0.0; __session_seq=4; __uv_seq=4; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1686135956',
    'Host': 'apic.liepin.com',
    'Origin': 'https://www.liepin.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.liepin.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Client-Type': 'web',
    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?inputFrom=head_navigation&scene=init&workYearCode=1&ckId=rc7wjmfwag9eis7k995hi2xx7sjj6dpb"}',
    'X-Fscp-Fe-Version': '',
    'X-Fscp-Std-Info': '{"client_id": "40108"}',
    'X-Fscp-Trace-Id': '296c6ffc-320c-4ab2-ab90-29e44a2664d4',
    'X-Fscp-Version': '1.1',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'p9QLPjJMQx-fu-i4zHjHkA'
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
    df.to_excel('liepin.xlsx')
    df = pd.read_excel('liepin.xlsx')
    df

    df_PM_gz =  df[['job.labels','job.refreshTime','job.title','job.salary','job.dq','job.topJob','job.requireWorkYears','job.requireEduLevel','comp.compStage','comp.compName','comp.compIndustry','comp.compScale']]
    df_PM_gz

    df_PM_gz['job.dq'].value_counts()
    地区 = [ df_PM_gz['job.dq'].value_counts().index.tolist()[i].split('-')[1]\
             for i,v in enumerate(df_PM_gz['job.dq'].value_counts().index.tolist()) if '-' in v]
    地区
    岗位个数 = [ df_PM_gz['job.dq'].value_counts().values.tolist()[i] for i,v in enumerate(df_PM_gz['job.dq'].value_counts().index.tolist()) if "-" in v]
    岗位个数
    from pyecharts import options as opts
    from pyecharts.charts import Map
    from pyecharts.faker import Faker

    c = (
        Map()
        .add(用户输入城市, [list(z) for z in zip(地区, 岗位个数)], 用户输入城市)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-地区地图"), visualmap_opts=opts.VisualMapOpts()
        )
        .render('hha.html')
    )
    return c