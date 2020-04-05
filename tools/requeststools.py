import requests

'''
requests.request(get/post) = requests.get/requests.post
'''
'''
    名称：
        自定义的请求方法
    参数：
        method：请求的方法
        Url：地址
        headers： 请求头
        jsondata ：json格式的接口参数
        httpcode ：http状态码
        ascode ： 接口返回的实际状态码
    返回值：
        ture : 通过
        false: 失败
'''
def request1(method, url, headers={}, jsondata={}, httpcode=200, ascode=200):
    """
    名称：
        自定义的请求方法
    参数：
        method：请求的方法
        Url：地址
        headers： 请求头
        jsondata ：json格式的接口参数
        httpcode ：http状态码
        ascode ： 接口返回的实际状态码
    返回值：
        ture : 通过
        false: 失败
    """
    res = requests.request(method,url=url,headers=headers,json=jsondata)
    try:
        assert res.status_code == httpcode
        assert ascode == res.json()['status']
        return True
    except:
        return False