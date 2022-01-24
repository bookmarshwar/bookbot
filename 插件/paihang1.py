from nonebot import on_command
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import escape,unescape, MessageEvent, Message, MessageSegment
import random
import httpx,json
import datetime,requests
from sign import*
ph=on_command("好感排行", priority=1)
@ph.handle()
async def handle_first_start(bot: Bot, event: Event, state: T_State):
    msg=""
    qqid=event.get_user_id()#获取qqid
    x=event.get_session_id()
    re = x.split('_')
    x=re.pop(1)
    args = str(event.get_message()).strip()
    name=account(qqid)
    db=name.accounts()
    if db[7]==0:
        cashname=""
    else:
        cashname=db[7]
    try:
        args=int(args)
    except:
        await ph.finish(f"{cashname}请跟随数字相信你不是傻蛋")
    if args>8:
        args=8
    dt=paihang()
    db=dt.haogan(args)
    for i in range(0,int(args)):
        try:
            demo=await bot.call_api("get_group_member_info",group_id=x,user_id=db[i][0])
        except:
            demo=await bot.call_api("get_stranger_info",user_id=db[i][0])
            demo['nickname']=f"其他群的{demo['nickname']}"
        if demo['nickname']=="其他群的":
            demo['nickname']="无用户信息"
        msg+=f"{i+1}.{demo['nickname']}:{db[i][1]}\n"
    await ph.finish(msg)