# import os
# import asyncio
import logging
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from filters.chat_types import ChatTypeFilter
from kbds import reply
from random import randint
global city_arr
from bd.myfile import city_arr
from aiogram.types import CallbackQuery

logging.basicConfig(level=logging.DEBUG)

help_city=''   
myarrray=[]
list_of_all=[]
list_of_used=[]
last_letter=''
l=''
h=''
ll=[]
lh=[]
s=''
bot_started=False

def in_start_game():
    global myarrray
    global list_of_all
    global list_of_used
    global last_letter
    global l
    global ll  
    global lh
    global s
    global h
   
    list_of_used=[]
    myarrray=city_arr.replace("'",'').split(', ')
    myarrray.sort()
    list_of_all=[x.lower() for x in myarrray]
    
    for i in list_of_all:
        l+=i[-1]
    ll=list(set(l))
    ll.sort()
    
    for k in list_of_all:
        h+=k[0]
    lh=list(set(h))
    lh.sort()
    s=''
      
    
in_start_game()
   

def my_check(checkmessage):
    if checkmessage.lower() in list_of_used:
        return 'Це місто вже було назване'
    if checkmessage.lower() in list_of_all:
        list_of_used.append(checkmessage.lower())
        list_of_all.remove(checkmessage.lower())
        last_letter=checkmessage.lower()[-1]
        if last_letter in ['ь','и']:
            last_letter=checkmessage.lower()[-2]
        return 'Таке місто є. Моє місто на букву '+last_letter.upper()+': '+my_answer(last_letter)
    else:
        return 'В базі таких міст не знайдено.'
        
    
    
def my_answer(las_let):
    lma=[]
    global myarrray
    global list_of_all
    global list_of_used
    global last_letter
    global l
    global ll  
    global lh
    global s
    global h
    
    if len(list_of_all)==0:
        return 'В базі більше нема міст. Гру завершено'
    for i in list_of_all:
        if i[0]==las_let:
            lma.append(i)
    if len(lma)==0:
        return 'В базі нема більше міст на таку букву. Дякую за гру'
    elif len(lma)==1:
        ll.remove(las_let)
        return lma[0]
    else:
        s=lma[randint(0,len(lma)-1)]
        list_of_used.append(s)
        list_of_all.remove(s)
        help_city=s
        return s.capitalize()
    
def helper(helpcity):
    global myarrray
    global list_of_all
    global list_of_used
    global last_letter
    global l
    global ll  
    global lh
    global s
    global h
    if helpcity=='':
        in_start_game()
        return('Хоч одне мiсто портiбно би знати=)')
    lma=[]
    last_letter=helpcity[-1]
    
    if last_letter in ['ь','и']:
            last_letter=helpcity[-2]
    if len(list_of_all)==0:
        print(len(list_of_all))
        return 'В базі більше нема міст. Гру завершено'
    for i in list_of_all:
        if i[0]==last_letter:
            lma.append(i)
    if len(lma)==0:
        print(last_letter)
        return 'В базі нема більше міст на таку букву. Дякую за гру'
    elif len(lma)==1:
        ll.remove(last_letter)
        return lma[0]
    else:
        s=lma[randint(0,len(lma)-1)]
        help_city=s
        return ('Можете написати місто '+(help_city).capitalize())
    
# def adder():
            

                      
user_private_router=Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

  
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привіт! Зіграємо? Для початку натисни "Давай починати". Якщо назва закінчується на "ь" або "и", беремо передостанню букву' ,reply_markup=reply.start_kb)

@user_private_router.message( Command('newgame'))
@user_private_router.message(F.text.lower().contains('давай'))
async def menu_cmd(message: types.Message):
    global bot_started
    bot_started=True
    in_start_game()
    await message.answer('Давай, введи назву міста')
    
@user_private_router.message(Command('endgame'))
@user_private_router.message(F.text=='Завершити гру')
async def endgame_cmd(message: types.Message):
    global bot_started
    bot_started=False
    in_start_game()
    await message.answer('Дякую за гру')

    
@user_private_router.message(Command('addcity'))
async def addcity_cmd(message: types.Message):
    await message.answer('ВВедіть нову назву', reply_markup=reply.add_kb)

@user_private_router.message(F.text=='ВВедіть нову назву')
async def addcity_cmd(message: types.Message):
    await message.answer('zhdu')
    # 'ВВедіть нову назву', reply_markup=reply.add_kb)

@user_private_router.callback_query(F.data=='help_inl_k')
async def help_inl_k(callback: CallbackQuery):
    await callback.answer(text='any',show_alert=True)
    await callback.message.answer('/helpme')

@user_private_router.message(Command('helpme'))
@user_private_router.message(F.text=='Підказка')
async def helpme_cmd(message: types.Message):
    await message.reply(helper(s))
    
@user_private_router.message(F.text)
async def check_cmd(message: types.Message):
    if bot_started==True:
        await message.answer(my_check(message.text), reply_markup=reply.help_inl_k)
    else:
        await message.reply('натисныть на початок гри')

        
        
        
        
                
                
                
    
    
    
    