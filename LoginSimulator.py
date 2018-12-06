from urllib import error, parse, request
from base64 import b64encode, b64decode
from http import cookiejar
from random import random
from lxml import etree

LOGIN_URL = 'http://ecard.scuec.edu.cn/loginstudent.action'
CAPTCHAURL = "http://ecard.scuec.edu.cn/homeLogin.action/getCheckpic.action?rand="+str(random()*10000)
TOPURL = 'http://ecard.scuec.edu.cn/pages/top.jsp'

def save_img(o):
    imagedata = b64decode(o.Get_Captcha())
    file = open('1.jpg', "wb")
    file.write(imagedata)
    file.close()


def get_td(resp):
    return etree.parse(resp_top.encode('utf-8')).xpath('//td')


class LoginSim:
    def __init__(self, LoginUrl, CaptchaUrl, TopUrl):
        """
        构造函数
        :param LoginUrl:登陆链接
        :param CaptchaUrl: 获取验证码链接
        """
        self.LoginUrl = LOGIN_URL
        self.CaptchaUrl = CaptchaUrl
        self.TopUrl = TopUrl
        # 实例化cookiejar管理器并托管整个生命周期cookie
        self.cookie = cookiejar.CookieJar()
        handler = request.HTTPCookieProcessor(self.cookie)
        self.opener = request.build_opener(handler)

    def Get_Captcha(self):
        """
        获取cookie=>SessionID
        :return: base64编码的验证码图片
        """
        return b64encode(self.opener.open(self.CaptchaUrl).read())

    def Login(self, rand, name, password):
        postData = {
            'name': name,
            'userType': '1',
            'passwd': password,
            'loginType': '2',
            'rand': rand,
            'imageField.x': '22',
            'imgaeField.y': '21'
        }
        headers = {
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image \
            / apng, * / *;q = 0.8',
            'Host': 'ecard.scuec.edu.cn',
            'Referer': 'http://ecard.scuec.edu.cn/homeLogin.action',
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit \
            / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.99Safari / 537.36'
        }
        postdata = parse.urlencode(postData)
        req = request.Request(self.LoginUrl, postdata.encode(), headers)
        self.opener.open(req)
        req_top = request.Request(self.TopUrl)
        return self.opener.open(req_top)

# o = LoginSim(LOGIN_URL, CAPTCHAURL, TOPURL)
# SecretCode = input('输入验证码： ')
# response = o.Login(SecretCode, '201621093013', '422001')

# print(response)