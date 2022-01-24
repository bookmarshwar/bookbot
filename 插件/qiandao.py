from nonebot import on_command
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import escape,unescape, MessageEvent, Message, MessageSegment
import random
import httpx,json
import datetime,requests
import time as nt
from sign import*
js = {}
def get_lis():#获取tis
    url='https://api.vvhan.com/api/ian'#可能会超时
    try:
        res=requests.get(url,timeout=1)
    
        return res.text
    except:
        return "完词穷了,记得不要当赌狗"
def random_haogan():
    x=random.randint(1,100)
    x=x/100
    return x
qiandao = on_command("签到", priority=1)
@qiandao.handle()
async def handle_first_start(bot: Bot, event: Event, state: T_State):
    qqid=event.get_user_id()#获取qqid
    name=account(qqid)#初始用户信息
    time=datetime.datetime.now().strftime('%Y-%m-%d')#获取时间
    db=name.accounts()
    print(db[7])
    if db[7]==0:
        cashname=""
    else:
        cashname=db[7]
    if db[4]==time:
        print(1)
        msgg=get_lis()#获取tisC
        await qiandao.finish(f"{cashname}你今天已经签到到过了!金币:{db[2]},好感:{db[1]}\ntips:{msgg}")
    else:
        name.update_time(time)
        haogan_num=random_haogan()
        haogan=float(db[1]+haogan_num)
        haogan=round(haogan,2)
        coin_num=random.randint(1,50)
        coin=float(db[2]+coin_num+haogan*5)
        coin=round(coin,2)
        name.update_conts(coin)
        name.update_time(time)
        name.update_haogan(haogan)
        await qiandao.send(f"签到成功!金币:{coin},好感:{haogan}")
        await qiandao.send(f"好感度+{haogan_num}\n金币+{coin_num}\n额外金币+{round(haogan*5,2)}")
        msgg=get_lis()#获取tis
        await qiandao.send(f"tips:{msgg}")
        await qiandao.finish()        
                                                                                                                                                                                                                  