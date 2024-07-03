from aiogram import Router, types, F
from aiogram.filters.command import Command
from utils.fox import fox
from keyboards.kb2 import kb1
from random import randint


router = Router()


@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Привет! Можешь мне написать, я отвечу тем же. Можешь использовать кнопочки ниже для доп. функций", reply_markup=kb1)


@router.message(Command("ура"))
async def send_ura(message: types.Message):
    await message.answer("УРАААА! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.", reply_markup=kb1)


@router.message(Command("fox"))
@router.message(Command("лиса"))
async def send_fox(message: types.Message):
    image_fox = fox()
    await message.answer_photo(image_fox)


@router.message(Command('num'))
async def send_random(message: types.Message):
    number = randint(1, 100)
    await message.answer(f"{number}")


@router.message(F.text)
async def echo(message: types.Message):
    if "ура" in message.text:
        await message.answer("УРАААА!")
    elif message.text == "инфо":

        user_name = message.chat.id
        print(user_name)
        await message.answer(str(user_name))
    else:
        await message.answer(message.text)