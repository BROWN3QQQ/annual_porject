from http import cookiejar
from urllib import error, parse, request
from random import random
from base64 import b64encode

LOGIN_URL = 'http://ecard.scuec.edu.cn/loginstudent.action'
CaptchaUrl = "http://ecard.scuec.edu.cn/homeLogin.action/getCheckpic.action?rand="+str(random()*10000)

class LoginSim:
    def __init__(self, LoginUrl, CaptchaUrl):
        """
        构造函数
        :param LoginUrl:登陆链接
        :param CaptchaUrl: 获取验证码链接
        """
        self.LoginUrl = LOGIN_URL;
        self.CaptchaUrl = CaptchaUrl;
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
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
            'Host': 'ecard.scuec.edu.cn',
            'Referer': 'http://ecard.scuec.edu.cn/homeLogin.action',
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.99Safari / 537.36'
        }
        postdata = parse.urlencode(postdata)
        request.Request(self.LoginUrl, postdata.encode(), headers)
        try:
            response = self.opener.open(request)
            # TODO 检查登陆结果
        except urllib.error.URLError as e:
            print(e.code, ':', e.reason)
# 以上是模拟登录并且获取cookie的代码
