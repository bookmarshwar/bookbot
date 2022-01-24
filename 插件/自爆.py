from nonebot import on_command
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import escape,unescape, MessageEvent, Message, MessageSegment
import random
import httpx,json
import datetime,requests
from sign import*
zb=on_command("自爆",priority=1)
@zb.handle()
async def handle_first_start(bot: Bot, event: Event, state: T_State):
    x=event.get_session_id()
    re = x.split('_')
    x=re.pop(1)
    args = str(event.get_message()).strip()
    args=args.split('qq=')
    args=args[1].split(']')#返回qq
    qqid=event.get_user_id()#获取qqid
    try:
        await bot.call_api('set_group_ban',group_id=x,user_id=args[0],duration=60)
        await bot.call_api('set_group_ban',group_id=x,user_id=qqid,duration=60)
        await zb.finish("害人害己")
    except:
        await zb.finish("目标等级似乎和bot同级或者更高\n(tis:bot可能不是管理或者群主)")