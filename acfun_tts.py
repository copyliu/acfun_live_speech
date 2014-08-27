#  -*- coding: UTF-8 -*-

import socket
from utils import *
import random
import time


import win32com.client

from dragonfly.engines.engine import get_sapi5_engine
engine = get_sapi5_engine()


def connect(ip="103.244.232.68",port=12006):

    s=socket.socket()
    s.settimeout(5)
    s.connect((ip,port))

    return s

def login(s,roomid,username="",password=""):
    if isinstance(s,socket.socket):
        data={}
        data["type"]="loginreq"
        data["username"]=username
        data["password"]=password
        data["roomid"]=roomid
        s.send(acfunencode(data))
        res=s.recv(65536)
        return acfundecode(res)

def keepalive(s):
    if isinstance(s,socket.socket):
        data={}
        data["type"]="keeplive"
        data["tick"]=random.randint(0,100)
        s.send(acfunencode(data))
        res=s.recv(65536)
        return acfundecode(res)

def waitfornewchat(s):
    if isinstance(s,socket.socket):
        s.settimeout(1)
        try:
            res=s.recv(65536)
        except:
            return []
        return acfundecode(res)
if __name__ =="__main__":

    print u"房間號碼: "
    roomid=raw_input()
    engine.speak(u"開始運作")
    s=connect()
    print "login as ",login(s,roomid)[0]["nickname"].decode("utf8")
    while 1:
        q=keepalive(s)
        for i in q:
            if isinstance(i,dict):
                if i.has_key("type"):
                    if i["type"]=="chatmessage":
                        if i.has_key("content") and i.has_key("snick"):
                            con= i["content"]
                            print i["snick"].decode("utf8")+":",con.decode("utf8")
                            engine.speak(con.decode("utf8"))


        time.sleep(1)



