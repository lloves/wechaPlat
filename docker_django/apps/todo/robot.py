# Filename: robot.py

from werobot import WeRoBot
from .XMLParser import HemslXMLParser
#from HemslXMLParser import *
from docker_django import settings

robot = WeRoBot(token='kuaishoudownloadswwww')


@robot.handler
def hello(message):
    mXmlParser = HemslXMLParser(settings.STRING_CONF_DIR)
    reply_msg = mXmlParser.getAttribVlue('subscribe_reply')
    return reply_msg.encode("unicode-escape").decode('unicode_escape')
    #return 'Hello World!'

@robot.subscribe
def subscribe(message):
    mXmlParser = HemslXMLParser(settings.STRING_CONF_DIR)
    return mXmlParser.getAttribVlue('subscribe_reply')
    #return '我是来自火星的极度智能机器人乐乐，我的神奇能力是助您『聊天破冰无尴尬』。\n\n1.点击菜单，选择您喜欢的那类型，乐乐就可以利用自己的大脑帮您在乐乐家族巨大的数据库里面匹配心仪的聊天对象。\n\n2.您和对面的她\他可以看到实时的聊天过程哦。时机到了您可以选择接管乐乐聊天，乐乐会躲在小角落默默不出声。\n\n你们开心就是乐乐最大的快乐。快来尝试吧。'
