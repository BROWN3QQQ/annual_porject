from .LoginSimulator import LoginSim
from urllib import error, parse, request
from random import random
from lxml import etree
from time import sleep

login_url = 'http://ecard.scuec.edu.cn/pages/card/cardMain.jsp'
captcha_url = "http://ecard.scuec.edu.cn/homeLogin.action/getCheckpic.action?rand=" + str(random() * 10000)


class Crawler(LoginSim):

    def __init__(self):
        LoginSim.__init__(self, login_url, captcha_url)
        self.headers = dict(
            get={
                'Host': 'ecard.scuec.edu.cn',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
                       /537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                'Referer': 'http://ecard.scuec.edu.cn/accleftframe.action'
            },
            post1={
                'Host': 'ecard.scuec.edu.cn',
                'Connection': 'keep-alive',
                'Content-Length': '52',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
                  /537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Referer': 'http://ecard.scuec.edu.cn/accounthisTrjn.action',
            },
            post2={
                'Host': 'ecard.scuec.edu.cn',
                'Connection': 'keep-alive',
                'Content-Length': '45',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
                  /537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Referer': 'http://ecard.scuec.edu.cn/accounthisTrjn1.action'
            },
            post3={
                'Host': 'ecard.scuec.edu.cn',
                'Connection': 'keep-alive',
                'Content-Length': '0',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
                  /537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Referer': 'http://ecard.scuec.edu.cn/accounthisTrjn2.action'
            })
        self.urls = dict(
            accoun_type_url='http://ecard.scuec.edu.cn/accounthisTrjn.action',
            posturl="http://ecard.scuec.edu.cn/accounthisTrjn{}.action",
            nextpage="http://ecard.scuec.edu.cn/accountconsubBrows.action")
        self.get_account_type = False
        self.postdata = dict(
            data1={
                'account': '20167',
                'inputStartDate': 'all',
                'Submit': '+%C8%B7+%B6%A8+'},
            data2={
                'inputEndDate': '20180903',
                'inputStartDate': '20181229'
            })

    def get_account(self):
        """
        获取账户类型
        :return: string 应填入postdata1中的account字段
        """
        account_req = request.Request(url=self.urls['account_type_url'], headers=self.headers['get'])
        try:
            account_res = self.opener.open(account_req)
        except error.URLError as e:
            return e
        account_res = account_res.read().decode('gb2312')
        tree = etree.HTML(account_res)
        result = tree.xpath('//*[@id="account"]/option')
        if len(result) < 1:
            return False
        else:
            self.postdata['data1']['account'] = result[0]['value']
            self.get_account_type = True
            return True

    def get_information(self):
        postdata = parse.urlencode(self.postdata['data1']).encode()
        first_req = request.Request(self.urls['posturl'].format('1'), postdata, self.headers['post1'])
        postdata = parse.urlencode(self.postdata['data2']).encode()
        second_req = request.Request(self.urls['posturl'].format('2'), postdata, self.headers['post2'])
        third_req = request.Request(self.urls['posturl'].format('3'), None, self.headers['post3'])
        try:
            self.opener.open(first_req)
            self.opener.open(second_req)
            sleep(1)
            result = self.opener.open(third_req)
        except error.URLError as e:
            return e
        return result
        # TODO 获取全量消费记录信息，需要生成迭代获取。

# headers = {
#     'Host': 'ecard.scuec.edu.cn',
#     'Connection': 'keep-alive',
#     'Content-Length': '0',
#     'Cache-Control': 'max-age=0',
#     'Origin': 'http://ecard.scuec.edu.cn',
#     'Upgrade-Insecure-Requests': '1',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
#                   /537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Referer': 'http://ecard.scuec.edu.cn/accleftframe.action',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
# }
# get_url = 'http://ecard.scuec.edu.cn/accleftframe.action'  # 利用cookie请求訪问还有一个网址
#
# get_request = request.Request(get_url, None, headers)
