from nonebot import on_command
from nonebot.rule import to_me,keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import escape,unescape, MessageEvent, Message, MessageSegment
import random
import httpx,json
import datetime,requests
from sign import*
pyounum=0
pbotnum=0
num_pan=0
p = on_command("21点", rule=keyword("21点"), priority=1)
@p.handle()
async def handle_first_start(bot: Bot, event: Event, state: T_State):
    
    global name
    qqid=event.get_user_id()#获取qqid
    name=account(qqid)
    await p.send("book提醒您,小赌怡情大赌伤身")
@p.got("num",prompt="请输入金额")
async def handle_first_start(bot: Bot, event: Event, state: T_State):
    global pyou,pyounum,pbotnum,pbot,num_pan,num
    pyounum=0#你的总点数
    pbotnum=0#机器人的总点数
    num_pan=0#传递输赢的值
    try:#判断是否是数字
        num=int(state["num"])
    except:
        await p.finish("已退出21点")
    if num <=0:
        await p.finish("已退出21点")
    if num> name.id_conts():#判断是否有足够的钱
        print(name.id_conts())
        await p.finish("穷光蛋,前面的地方以后在来探索吧")
    pyou=point()
    pbot=point()
    pyounum=pyounum+pyou
    pbotnum=pbotnum+pbot
    await p.send(f"你抽到了{pyou}点,目前总共{pyounum}点")
@p.got("word",prompt="是否继续抽牌(继续/不继续)")
async def handle_first_start(bot: Bot, event: Event, state: T_State):
    global pyou,pyounum,pbotnum,pbot,num_pan
    word=state["word"]
    if word =="继续":
        pyou=point()
        pyounum=pyounum+pyou
        if pyounum <=21:
            await p.reject(f"你抽到了{pyou}点,目前总共{pyounum}点,是否继续抽牌")
        else:
            await p.send(f"你抽到了{pyou}点,目前总共{pyounum}点,你大于了21点,你输了")
            name.update_conts(name.id_conts()-num)#存入数据
            await p.finish(f"下次记得赢回来哦,你输了{num}摩拉")
    elif word == "不继续":
        await p.send("你选择了停牌,轮到机器人抽牌")
    else:
        await p.reject("听不懂人话是吧,让你选继续还是不继续")
@p.handle()
async def handle_first_start(bot: Bot, event: Event, state: T_State):
    global pbot,pbotnum
    pbot=point()
    pbotnum=pbotnum+pbot#机器人决定抽牌
    while pbotnum<=21:
        if pbotnum <=21:
            await p.send(f"book抽到了{pbot}点,目前总共{pbotnum}点")
            pbot=point()
            pbotnum=pbotnum+pbot
        else:
            break
    pbotnum=pbotnum-pbot
    await p.send(f"book停止了抽牌,book现在{pbotnum}点,你现在{pyounum}点")
    
    if pbotnum==pyounum:
        await p.finish("平局了,下次还要在来哦")

    elif pbotnum>pyounum:
        name.update_conts(name.id_conts()-num)
        await p.finish(f"下次记得赢回来哦,你输了{num}摩拉")
    else:
        name.update_conts(name.id_conts()+num)
        await p.finish(f"下次我一定赢回来的,虽然你赢了{num}摩拉")  


    
    