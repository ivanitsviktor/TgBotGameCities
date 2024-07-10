from aiogram.types import BotCommand
from telegram import CallbackQuery


private=[
    BotCommand(command='start',description='Зіграємо?'),
    BotCommand(command='newgame',description='Розпочати нову гру'),
    BotCommand(command='endgame',description='Завершити гру'),
    BotCommand(command='addcity',description='Додати новеий населений пункт'),
    BotCommand(command='helpme', description='Підкажи місто'),
]
group=[BotCommand(command='start',description='zigraemo'),]


# start-Зіграємо?
    # newgame-Нова гра
    # endgame-Гру завершено
    # addcity-Додаєто місто