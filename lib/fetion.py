#!/usr/bin/python
# coding: utf-8
import _envi
import requests
from lerrylib.extract import extract
from config import Fetion
from lib.signal import SIGNAL

url_login = 'http://f.10086.cn/im5/login/loginHtml5.action'
url_logout = 'http://f.10086.cn/im5/index/logoutsubmit.action'
msg_url = 'http://f.10086.cn/im5/chat/sendNewMsg.action'
sms_url = 'http://f.10086.cn/im5/chat/sendNewGroupShortMsg.action'

login_data = {
    'pass': Fetion.pw,
    'm' : Fetion.no,
    'captchaCode':'',
    'checkCodeKey':'null'
}

@SIGNAL.send_sms
def send_sms(msg):
    s = requests.session()
    s.post(url_login, data=login_data)
    #r = s.post(msg_url, data={'touserid':'526862966', 'msg':'测11试'})
    r = s.post(sms_url, data={'msg':msg, 'touserid':',526862966'})
    print r.text
    s.post(url_logout)

if __name__ == '__main__':
    for i in range(100):
        send_sms('nihao %s' % i)