
import logging
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from filters.chat_types import ChatTypeFilter
from kbds import reply
from random import randint
global city_arr
from bd.myfile import city_arr
import wikipediaapi

logging.basicConfig(level=logging.DEBUG)


def is_city(word):
    wiki_wiki = wikipediaapi.Wikipedia('google.com', 'uk')
    page=wiki_wiki.page(word)
    if page.exists():
        categories = page.categories
        for category in categories.keys():
            if 'Населені пункти' in category:
                list_of_all.append(word.lower())
                filename = 'bd/myfile.py'
                with open(filename, 'r', encoding='utf-8') as file:
                    content = file.read()
                new_content = 'city_arr="' + content[10:-1]+', '+word.upper() + '"'
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(new_content)
        
                return 'misto dodano'
    return 'ne naspunkr'
        
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
    for k in list_of_all:
        h+=k[0]
    lh=list(set(h))
    s=''
    
in_start_game()

def my_check(checkmessage):
    global bot_started
    global last_letter 
    global list_of_all
    global list_of_used
    if checkmessage.lower() in list_of_used:
        return 'Це місто вже було назване'
    if checkmessage.lower() in list_of_all:
        if list_of_used==[]:
            list_of_used.append(checkmessage.lower())
            list_of_all.remove(checkmessage.lower())
            last_letter=checkmessage.lower()[-1]
            if last_letter in ['ь','и']:
                last_letter=checkmessage.lower()[-2]
            return 'Таке місто є. Моє місто на букву '+last_letter.upper()+': '+my_answer(last_letter)
        else:
            if last_letter==checkmessage[0].lower():
                list_of_used.append(checkmessage.lower())
                list_of_all.remove(checkmessage.lower())
                last_letter=checkmessage.lower()[-1]
                if last_letter in ['ь','и']:
                    last_letter=checkmessage.lower()[-2]
                return 'Таке місто є. Моє місто на букву '+last_letter.upper()+': '+my_answer(last_letter)
        return 'ne ta bukva'    
            
    else:
        # bot_started=False
        return 'В базі таких міст не знайдено. '
        
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
    global bot_started
    
    if len(list_of_all)==0:
        return 'В базі більше нема міст. Гру завершено'
    for i in list_of_all:
        if i[0]==las_let:
            lma.append(i)
    if len(lma)==0:
        bot_started=False
        return 'В базі нема більше міст на таку букву. Дякую за гру'
    elif len(lma)==1:
        ll.remove(las_let)
        return lma[0]
    else:
        s=lma[randint(0,len(lma)-1)]
        list_of_used.append(s)
        list_of_all.remove(s)
        last_letter=s[-1]
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
    global lma
    global bot_started
    if helpcity=='':
        in_start_game()
        return('Хоч одне мiсто портiбно би знати=)')
    lma=[]
    last_letter=helpcity[-1]
    
    if last_letter in ['ь','и']:
            last_letter=helpcity[-2]
    if len(list_of_all)==0:
        return 'В базі більше нема міст. Гру завершено'
    for i in list_of_all:
        if i[0]==last_letter:
            lma.append(i)
    if len(lma)==0:
        bot_started=False
        return 'В базі нема більше міст на таку букву. Дякую за гру'
    else:
        s=lma[randint(0,len(lma)-1)]
        help_city=s
        return ('Можете написати місто '+(help_city).capitalize())
    
user_private_router=Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

  
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    bot_started=False
    await message.answer('Привіт! Зіграємо? Для початку натисніть "Нова гра". Якщо назва населеного пункту закінчується на "ь" або "и", беремо передостанню букву' ,reply_markup=reply.start_kb)

@user_private_router.message( Command('newgame'))
@user_private_router.message(F.text.lower().contains('нова гра'))
async def menu_cmd(message: types.Message):
    global bot_started
    bot_started=True
    in_start_game()
    await message.answer('Введіть назву міста')
    
@user_private_router.message(Command('endgame'))
@user_private_router.message(F.text=='Завершити гру')
async def endgame_cmd(message: types.Message):
    global bot_started
    bot_started=False
    in_start_game()
    await message.answer('Дякую за гру')
    
@user_private_router.message(F.text=='/addcity')
# Command('addcity')
async def addcity_cmd(message: types.Message):
    await message.answer('Щоб додати населений пункт, наберіть /addcity "Назва населеного пунту"')

@user_private_router.message(F.text.contains('/addcity '))
async def addcity_cmd(message: types.Message):
    await message.answer(is_city(message.text.replace('/addcity ','').strip()))

@user_private_router.message(Command('helpme'))
@user_private_router.message(F.text=='Підказка')
async def helpme_cmd(message: types.Message):
    if bot_started==True:
        await message.reply(helper(s))
    else:
        await message.reply('Натисніть на початок гри')
        
@user_private_router.message(F.text)
async def check_cmd(message: types.Message):
    if bot_started==True:
        await message.answer(my_check(message.text))
    else:
        await message.reply('Натисніть на початок гри')
        
   

        
        
        
        
                
                
                
    
    
    
    