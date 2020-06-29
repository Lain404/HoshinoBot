import time
import os

from nonebot import get_bot
from nonebot import CommandSession, MessageSegment
from nonebot import permission as perm
from peewee import fn
from .data import Question
from hoshino.service import Service, Privilege as Priv
answers = {}
answersRegex = {}
sv = Service('Q&A', manage_priv=Priv.ADMIN, enable_on_default=False)


# recovery from database
for qu in Question.select().where(Question.allow_private == 0):
    answers[qu.quest] = {}

for qu in Question.select().where(Question.allow_private == 1):
    answersRegex[qu.quest] = {}

@sv.on_message('group')
async def handle(bot, context):
    message = context['raw_message']
    if message.startswith('问UE'):
        msg = message[3:].split('答', 1)
        if len(msg) == 1:
            return
        q, a = msg
        q = q.strip()
        answersRegex[q] = {}
        Question.replace(
            quest=q,
            rep_group=context['group_id'],
            rep_member=1,
            allow_private=1,
            answer=a,
            creator=context['user_id'],
            create_time=time.time(),
        ).execute()
        await bot.send(context, f'好的我记住了', at_sender=False)
        return
    elif message.startswith('问'):
        msg = message[1:].split('答', 1)
        if len(msg) == 1:
            return
        q, a = msg
        q = q.strip()
        answers[q] = {}
        Question.replace(
            quest=q,
            rep_group=context['group_id'],
            rep_member=1,
            answer=a,
            creator=context['user_id'],
            create_time=time.time(),
        ).execute()
        await bot.send(context, f'好的我记住了', at_sender=False)
        return
    elif message.startswith('不要回答') or message.startswith('删除问题'):
        q = context['raw_message'][4:]
        q = q.strip()
        if context['user_id'] == 821046219:
            await bot.send(context, f'你没有权限删除问题奥~', at_sender=False)
            return
        if q.isdigit():
            line = Question.delete().where(
                Question.id == q,
                Question.rep_group == context['group_id']
            ).execute()
            if line>0:
                await bot.send(context, f'删除回答ID[{q}]成功', at_sender=False)
                return
            else:
                await bot.send(context, f'查无此回答奥~', at_sender=False)
                return
        else:
            await bot.send(context, f'请输入ID删除回答~', at_sender=False)


    elif message.startswith('查看问题'):
        q = context['raw_message'][4:]
        q = q.strip()
        ans = context['raw_message'] in answers.keys() | context['raw_message'] in answersRegex.keys()
        if ans:
            await bot.send(context, f'我不记得有这个问题', at_sender=False)
            return
        ans = '问题"' + q + '"的回答: '
        flag = False
        for que in Question.select().where(Question.quest == q, Question.rep_group == context['group_id'], Question.rep_member == 1):
            ans +=  '\n' + 'ID:' + str(que.id) + ' | ' + que.answer
            flag = True
        if flag:
            await bot.send(context, ans, at_sender=False)
            return
        else:
            await bot.send(context, f'我不记得有这个问题', at_sender=False)
            return
    elif context['raw_message'] in answers.keys():
        ans = ''
        for que in Question.select().where(Question.quest == context['raw_message'], Question.rep_group == context['group_id'], Question.rep_member == 1, Question.allow_private == 0).order_by(fn.Random()):
            ans = que.answer
            break
        if ans:
            await bot.send(context, ans, at_sender=False)
            return
        else:
            if ans:
                await bot.send(context, ans, at_sender=False)
                return
    else:
        flag = False;
        q = ''
        for key in answersRegex:
            if key in context['raw_message']:
                q = key
                flag = True
                break
        if flag:
            ans = ''
            for que in Question.select().where(Question.quest == q, Question.rep_group == context['group_id'], Question.rep_member == 1, Question.allow_private == 1).order_by(fn.Random()):
                ans = que.answer
                break
            if ans:
                await bot.send(context, ans, at_sender=False)
                return

