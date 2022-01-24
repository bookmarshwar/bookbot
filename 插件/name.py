from nonebot import on_command
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import escape,unescape, MessageEvent, Message, MessageSegment
import random
import httpx,json
import datetime,requests
from sign import*
name=on_command("以后就叫我", priority=1)
@name.handle()
async def handle_first_start(bot: Bot, event: Event, state: T_State):
    qqid=event.get_user_id()#获取qqid
    args = str(event.get_message()).strip()
    names=account(qqid)#初始用户信息
    if "苏苏"in args:
        args="苏苏的儿"
    names.update_name(args)
    await name.finish(f"好的,{args}")