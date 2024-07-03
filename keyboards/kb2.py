from aiogram import types

button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/num')
button3 = types.KeyboardButton(text='/camera')
button4 = types.KeyboardButton(text='/fox')
button5 = types.KeyboardButton(text='4')
button6 = types.KeyboardButton(text='8')
button7 = types.KeyboardButton(text='12')
button8 = types.KeyboardButton(text='16')



keyboard1 = [
    [button1, button2],
    [button3, button4]
]

keyboard2 = [
    [button1, button2],
    [button3, button4],
    [button5, button3]
]

keyboard3 = [
    [button5, button6],
    [button7, button8]
]


kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=False)
kb3 = types.ReplyKeyboardMarkup(keyboard=keyboard3, resize_keyboard=True)
