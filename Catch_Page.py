from urllib import error, parse, request
from base64 import b64decode
from random import random
from .LoginSimulator import LoginSim


# 验证码地址和post地址
LOGIN_URL = 'http://ecard.scuec.edu.cn/pages/card/cardMain.jsp'
CaptchaUrl = "http://ecard.scuec.edu.cn/homeLogin.action/getCheckpic.action?rand="+str(random()*10000)



以下是请求一个页面

headers = {
    'Host': 'ecard.scuec.edu.cn',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://ecard.scuec.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://ecard.scuec.edu.cn/accounthisTrjn2.action',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
get_url = 'http://ecard.scuec.edu.cn/accleftframe.action'  # 利用cookie请求訪问还有一个网址
'''
# get_request = urllib.request.Request(get_url,None,headers)
# get_response = opener.open(get_request)
# print(get_response.read().decode("gb2312"))
'''
# cookie_filename1 = 'cookie1.txt'
# cookie1 = http.cookiejar.MozillaCookieJar(cookie_filename1)
# handler1 = urllib.request.HTTPCookieProcessor(cookie1)
# opener1 = urllib.request.build_opener(handler1)

get_request = urllib.request.Request(get_url, None, headers)
try:
    response1 = opener.open(get_request)
    page1 = response1.read().decode("gb2312")
    print(page1)
except urllib.error.URLError as e:
    print(e.code, ':', e.reason)

cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
print(cookie)

# 以下是请求另外一个页面


postUrl1 = "http://ecard.scuec.edu.cn/accounthisTrjn1.action"
postUrl2 = "http://ecard.scuec.edu.cn/accounthisTrjn2.action"
postUrl3 = "http://ecard.scuec.edu.cn/accounthisTrjn3.action"

# 根据抓包信息 构造表单
headers1 = {
    'Host': 'ecard.scuec.edu.cn',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://ecard.scuec.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://ecard.scuec.edu.cn/accounthisTrjn.action',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'JSESSIONID=2BAD15A8E3FCF0FF07121FF98700D026'
}

headers2 = {
    'Host': 'ecard.scuec.edu.cn',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://ecard.scuec.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://ecard.scuec.edu.cn/accounthisTrjn1.action',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'JSESSIONID=2BAD15A8E3FCF0FF07121FF98700D026'
}

headers3 = {
    'Host': 'ecard.scuec.edu.cn',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://ecard.scuec.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://ecard.scuec.edu.cn/accounthisTrjn2.action',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'JSESSIONID=2BAD15A8E3FCF0FF07121FF98700D026'
}

postData1 = {
    'account': '20167',
    'inputStartDate': 'all',
    'Submit': '+%C8%B7+%B6%A8+'
}
postdata1 = urllib.parse.urlencode(postData1).encode()

postData2 = {
    'inputEndDate': '20181129',
    'inputStartDate': '20180929'
}
postdata2 = urllib.parse.urlencode(postData2).encode()

request = urllib.request.Request(postUrl2, postdata , headers2)
request1 = urllib.request.Request(postUrl3, None, headers3)
try:
    response = opener.open(request1)
    page = response.read().decode("gb2312")
    print(page)
except urllib.error.URLError as e:
    print(e.code, ':', e.reason)

# cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
# print(cookie)
# for item in cookie:
#     print('Name = ' + item.name)
#     print('Value = ' + item.value)