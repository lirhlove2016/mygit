#coding:utf-8

from dingtalkchatbot.chatbot import DingtalkChatbot

ding_webhook="https://oapi.dingtalk.com/robot/send?access_token="
ding_token=""
message=("this is testing message")

if ding_token:
    ding_robot=DingtalkChatbot(ding_webhook+ding_token)
    ding_robot.sent_text(message)
else:
    print('dingding robot token is null, can not send ding ding msg')
