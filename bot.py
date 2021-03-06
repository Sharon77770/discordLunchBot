import discord
import os
from random import *
from discord.ext.commands import Bot
from discord.utils import get
from urllib import request
from bs4 import BeautifulSoup
from datetime import date, timedelta


intents=discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)



def getTodayMenu(sourece):
    print(str(sourece))
    
    today = date.today()
    tomorrow = date.today() + timedelta(1)

    splitTarget = str(today.month) + '월 ' + str(today.day) + '일 [점심]'

    if str(sourece).find(splitTarget) == -1 :
        return '급식이 없습니다.'

    newMsg = str(sourece).split(splitTarget)[1]

    if tomorrow.month == today.month :
        splitTarget = str(tomorrow.month) + '월 ' + str(tomorrow.day) + '일'
        newMsg = newMsg.split(splitTarget)[0]

    mList = newMsg.split(' ')

    msg = ''

    for i in range(len(mList)) :
        msg += mList[i] + '\n'

    print(msg)

    return msg

    






@bot.command()
async def 자살(ctx):
    target = request.urlopen('http://www.koreawqi.go.kr/wQSCHomeLayout_D.wq?action_type=T#')
    soup = BeautifulSoup(target,'html.parser')
    msg = soup.find('tr', class_='site_S01001').find_next_sibling("tr").text
    str1 = str(msg)
    str1 = str1.split('\n')
    if str1[3] == '통신오류':
        await ctx.send('통신 오류로 현재 수온을 확인할 수 없습니다.\n자세한 사항은 http://www.koreawqi.go.kr/wQSCHomeLayout_D.wq?action_type=T# 를 참고해주세요.')
    elif str1[3] == '장비점검':
        await ctx.send('장비 점검으로 현재 수온을 확인할 수 없습니다.\n자세한 사항은 http://www.koreawqi.go.kr/wQSCHomeLayout_D.wq?action_type=T# 를 참고해주세요.')
    else:
        str1 = str1[4].split('\t')
        str1 = str1[13].split('\r')
        msg = str1[0]
        await ctx.send('현재 한강물의 온도는 ' + msg + '도 입니다.' + ctx.author.mention + '님께서 뛰어내리기 딱 좋은 온도네요^^')




@bot.command()
async def 급식(ctx):
    target = request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=1&acr=2&acq=%EB%8F%99%EC%9B%90&qdt=0&ie=utf8&query=%EB%8F%99%EC%9B%90%EA%B3%A0+%EA%B8%89%EC%8B%9D')

    soup = BeautifulSoup(target,'html.parser')

    msg = soup.find_all(attrs={'class':'school_menu _page_panel'})
    
    menu = getTodayMenu(msg)
    
    await ctx.send('' + menu)
    

#bot.run(os.environ['token'])
bot.run('ODY2NjAzOTI1Nzk2MjkwNTYw.YPU9zA.eGInYWyiOu_EykO1H0HyO1I85FM')