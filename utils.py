#  -*- coding: UTF-8 -*-
__author__ = 'Administrator'
import struct

acfun_magic_num=689

def acfunencode(d):
    """
    类似urllib.urlencode()的功能 不过是给ACFUN用的
    :param d: @type dict
    :return: str
    """
    result=""
    if isinstance(d,dict):
        for k,v in d.items():
            result += "%s@=%s/" % (k, v)
        result=str(result)
        result=struct.pack("I",len(result)+9)+struct.pack("I",len(result)+9)+struct.pack("I",acfun_magic_num)+result
        result+="\x00"
        return result

    else:
        return ""

def acfundecode(d):
    """
    这个是解码的
    :param d:str
    :return : dict
    """
    if len(d)<12:
        return {}

    start=0
    ent=d
    result=[]
    while ent:
        if len(ent)<4:return result
        length=struct.unpack("I",d[start:start+4])[0]
        ent=d[start+12:start+4+length]
        start=start+4+length
        dic={}

        body=ent.split("/")
        for i in body:
            if not i:continue
            entry=i.split("@=")
            if len(entry)<2:continue
            dic[entry[0]]=entry[1]
        result.append(dic)
        ent=d[start:]

    return result
