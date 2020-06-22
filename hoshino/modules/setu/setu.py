import os
import re
import time
import random

from nonebot import on_command, CommandSession, MessageSegment, NoneBot
from nonebot.exceptions import CQHttpError

from hoshino import R, Service, Privilege
from hoshino.util import FreqLimiter, DailyNumberLimiter
stop_list = [
    '你已经冲了好多次了，明天再来吧',
    '？？？',
	'？',
	'不要涩图不要涩图',
	'你弟弟还好吗？',
    '别充了去玩PCR吧',
    '拿去冲！',
]
stop = random.choice(stop_list)
#configjson的使用
_max = 3
EXCEED_NOTICE = f'{stop}'
#次数限制计数器
_nlmt = DailyNumberLimiter(_max)
#频率限制计数器
_flmt = FreqLimiter(5)

'setu=D:\Github\HoshinoBot\res-20200501\img\setu'
sv = Service('setu', manage_priv=Privilege.SUPERUSER, enable_on_default=True, visible=False)
setu_folder = R.img('setu/').path

#生成另一组图片选择器
#setu2_folder = R.img('setu2/').path
def setu_gener():
    while True:
        filelist = os.listdir(setu_folder)
        random.shuffle(filelist)
        for filename in filelist:
            if os.path.isfile(os.path.join(setu_folder, filename)):
                yield R.img('setu/', filename)

setu_gener = setu_gener()

def get_setu():
    return setu_gener.__next__()

@sv.on_rex(re.compile(r'我还能冲|我还可以冲|我身体很好'), normalize=True)
async def seturefresh(bot:NoneBot, ctx, match):	
    uid = ctx['user_id']
    _nlmt.reset(uid)
    await bot.send(ctx, f"你觉得你又行了？", at_sender=True)

@sv.on_rex(re.compile(r'不够[涩瑟色]|[涩瑟色]图|来一?[点份张].*[涩瑟色]|再来[点份张]|看过了|炼铜|我是lsp'), normalize=True)
async def setu(bot:NoneBot, ctx, match):
    """随机叫一份涩图，对每个用户有冷却时间"""
    uid = ctx['user_id']
    if not _nlmt.check(uid):
        stop = random.choice(stop_list)
        #EXCEED_NOTICE = f'{stop}'
        #注册的命令主体是bot，所以使用bot.send hourcall 没有命令主题
        pic = R.img(f"antisetu{random.randint(1, 3)}.jpg").cqcode
        await bot.send(ctx, f"{stop}\n{pic}", at_sender=True)
        return

    if not _flmt.check(uid):
        await bot.send(ctx, '您冲得太快了，请稍候再冲', at_sender=True)
        return

     #概率阻止
    #if random.random()>0.6:
    #await session.send(f"不理你啦！バーカー\n{pic}", at_sender=True)
    #    return		
    #pic = R.img(f"chieri{random.randint(1, 4)}.jpg").cqcode
    #await session.send(f"不理你啦！バーカー\n{pic}", at_sender=True)
    # conditions all ok, send a setu.
    _flmt.start_cd(uid)
    _nlmt.increase(uid)
    pic = get_setu()
    try:
        await bot.send(ctx, pic.cqcode)
    except CQHttpError:
        sv.logger.error(f"发送图片{pic.path}失败")
        try:
            await bot.send(ctx, '涩图太涩，发不出去勒...')
        except:
            pass
