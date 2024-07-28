# from aiogram import types
# from aiogram.types import CallbackQuery
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)



start_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Нова гра'),
        KeyboardButton(text='Підказка'),        
        # KeyboardButton(text='Додати назву'),
    ],[KeyboardButton(text='Завершити гру'),]
    ],
    resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Зробіть вибір")

# add_kb=ReplyKeyboardMarkup(
#     keyboard=[
#         [
#         KeyboardButton(text='Перевірити')
#         ],
#     ],
#     resize_keyboard=True,input_field_placeholder='Назва')

# InlineKeyboardMarkup(
#     inline_keyboard=[
#     [
#         InlineKeyboardButton(text='pereviryty nazvu',callback_data='perevirka'),
#         InlineKeyboardButton(text='vidmina',callback_data='vidmina')]
#         ],
#         resize_keyboard=True)

