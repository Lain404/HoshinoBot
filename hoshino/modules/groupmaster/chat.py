import random
from datetime import timedelta

from nonebot import on_command, CommandSession, MessageSegment, NoneBot
from hoshino import util
from hoshino.res import R
from hoshino.service import Service, Privilege as Priv

# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？', 'UE？', '优依？', 'UE', '优依'))
async def say_hello(session):
    await session.send('骑士君，我一直在你身边！')

sv = Service('chat', manage_priv=Priv.SUPERUSER, visible=False)

@sv.on_command('沙雕机器人', aliases=('笨蛋机器人','笨蛋UE','沙雕机器人','祖安机器人','祖安机器人','祖安机器人','祖安机器人',), only_to_me=False)
async def say_sorry(session):
    await session.send('ごめんなさい！嘤嘤嘤(〒︿〒)')

@sv.on_command('老婆', aliases=('waifu', 'laopo', '亲亲'), only_to_me=True)
async def chat_waifu(session):
    if not sv.check_priv(session.ctx, Priv.SUPERUSER):
        await session.send(R.img('laopo.jpg').cqcode)
    else:
        await session.send('爱你哟~mua~')

@sv.on_command('老公', only_to_me=True)
async def chat_laogong(session):
    await session.send('你给我滚！', at_sender=True)

@sv.on_command('mua',aliases=('么么','么么哒'), only_to_me=True)
async def chat_mua(session):
    await session.send('笨蛋~', at_sender=True)

@sv.on_command('来点星奏', only_to_me=True)
async def seina(session):
    await session.send(R.img('星奏.png').cqcode)

@sv.on_command('我有个朋友说他好了', aliases=('我朋友说他好了', ), only_to_me=True)
async def ddhaole(session):
    await session.send('那个朋友是不是你弟弟？')
    #await util.silence(session.ctx, 30)

@sv.on_command('我好了',aliases=('我冲好了', '我已经好了'), only_to_me=True)
async def nihaole(session):
    await session.send('不许好，憋回去！')

BANNED_WORD = (
    'rbq', 'RBQ', '憨批', '废物', '死妈', '崽种', '傻逼', '傻逼玩意',
    '没用东西', '傻B', '傻b', 'SB', 'sb', '煞笔', 'cnm', '爬', 'kkp',
    'nmsl', 'D区', '口区', '我是你爹', 'nmbiss', '弱智', '给爷爬', '杂种爬','憨憨爬','憨憨'
)
#@on_command('ban_word', aliases=BANNED_WORD, only_to_me=True)

@sv.on_command('Rbq', aliases=BANNED_WORD, only_to_me=True)
async def nihaole(session):
    pic = R.img(f"antiqmark{random.randint(4, 10)}.jpg").cqcode
    await session.send( f"{pic}", at_sender=True)
    await util.silence(session.ctx, 60)

# ============================================ #
'''
pic = R.img(f"xiwang{random.randint(1, 4)}.jpg").cqcode
await bot.send(ctx, f"{pic}", at_sender=True)
'''

@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.2:
        await bot.send(ctx, R.img('确实.jpg').cqcode)

@sv.on_keyword(('会战', '刀'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.2:
        await bot.send(ctx, R.img('我的天啊你看看都几点了.jpg').cqcode)

@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.2:
        await bot.send(ctx, R.img('内鬼.jpg').cqcode)

@sv.on_keyword(('没mana','没有mana','缺mana','mana没了'))
async def chat_mana(bot, ctx):
    if random.random() < 0.5:
        await bot.send(ctx, R.img('lackmana.jpg').cqcode)
		
@sv.on_keyword(('希望'))
async def chat_xiwang(bot, ctx):
    if random.random() < 0.5:
        pic = R.img(f"xiwang{random.randint(1, 5)}.jpg").cqcode
        await bot.send(ctx, f"{pic}", at_sender=False)

Q_WORD = ('？', '？？','？？？', )
@sv.on_keyword(Q_WORD)
async def chat_Q(bot, ctx):
    if random.random() < 0.2:
        pic = R.img(f"antiqmark{random.randint(1, 3)}.jpg").cqcode
        await bot.send(ctx, f"{pic}", at_sender=False)

@sv.on_keyword(('复读'))
async def chat_fudu(bot, ctx):
    if random.random() < 0.4:
        pic = R.img(f"fudu{random.randint(1, 5)}.jpg").cqcode
        await bot.send(ctx, f"{pic}", at_sender=False)

@sv.on_keyword(('心情复杂'))
async def chat_xinqingfuza(bot, ctx):
    if random.random() < 0.4:
        pic = R.img(f"fuza{random.randint(1, 1)}.jpg").cqcode
        await bot.send(ctx, f"{pic}", at_sender=False)

@sv.on_keyword(('氪金'))
async def chat_kejin(bot, ctx):
    if random.random() < 0.4:
        pic = R.img(f"kejin{random.randint(1, 2)}.jpg").cqcode
        await bot.send(ctx, f"{pic}", at_sender=False)

@sv.on_keyword(('群主'))
async def chat_qunzhu(bot, ctx):
    if random.random() < 0.2:
        await bot.send('群主快点女装！')
