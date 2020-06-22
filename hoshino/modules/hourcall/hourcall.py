import pytz
import random
import math
from hoshino.res import R
from datetime import datetime
from hoshino import util
from hoshino.service import Service


sv = Service('hourcall', enable_on_default=False)
'''
def get_hour_call():
    """从HOUR_CALLS中挑出一组时报，每日更换，一日之内保持相同"""
    config = util.load_config(__file__)
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    hc_groups = config["HOUR_CALLS"]
    g = hc_groups[ now.day % len(hc_groups) ]
    return config[g]
'''	

'''
@sv.scheduled_job('cron', hour='*')
async def hour_call():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    if 2 <= now.hour <= 5:
        return  # 宵禁 免打扰
    msg = get_hour_call()[now.hour]
    await sv.broadcast(msg, 'hourcall', 0)
'''	

@sv.scheduled_job('cron', hour='*')
async def hour_call():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    if 2 <= now.hour <= 5:
        return  # 宵禁 免打扰
    h=now.hour
    if(math.fmod(h,6)==0):
        pic = R.img(f"buyexp{random.randint(1, 2)}.jpg").cqcode
        msg = [ f'{pic} '  ]
        await sv.broadcast(msg, 'hourcall', 0)
        return
    pic = R.img(f"timer{random.randint(1, 2)}.jpg").cqcode
    msg = [ f'现在是{now.hour}点咯~~\n{pic} '  ]
    await sv.broadcast(msg, 'hourcall', 0)
    #msg = [ f'{pic} 【{i[2].strftime(r"%Y-%m-%d %H:%M")}】\n▲下载 {i[0]}' for i in new_bangumi ]    

    #await bot.send(f"UE~\n{pic}")
	
@sv.on_command('时间', only_to_me=True)
async def chat_laogong(session):
    now = datetime.now(pytz.timezone('Asia/Shanghai'))

    msg = get_hour_call()[now.hour]
    await sv.broadcast(msg, 'hourcall', 0)