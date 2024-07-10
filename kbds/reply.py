from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)



start_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Давай починати'),
        KeyboardButton(text='Підказка'),        
        # KeyboardButton(text='Додати назву'),
    ],[KeyboardButton(text='Завершити гру'),]
    ],
    resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Зробіть вибір")

add_kb=InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='pereviryty nazvu',url='https://youtube.com'),
        InlineKeyboardButton(text='vidmina',url='https://youtube.com')]
        ],
        resize_keyboard=True)

help_inl_k=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='pidkazka', callback_data='help_inl_k')],
    ]
)