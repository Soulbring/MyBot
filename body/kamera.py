from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.kb1 import make_row_keyboard
from keyboards.kb2 import kb1, kb3

router = Router()

available_system = [
    "IP система",
    "AHD система",
]

available_quality = ['1.3mp', '2mp', '5mp']

available_count = [range(1, 255)]

class ChoiceProfile(StatesGroup):
    sys = State()
    quality = State()
    count = State()

@router.message(Command("camera"))
async def command_camera(message: types.Message, state: FSMContext):
    await message.answer(
        text="Выберите видеосистему",
        reply_markup=make_row_keyboard(available_system)
    )
    await state.set_state(ChoiceProfile.sys)

@router.message(ChoiceProfile.sys, F.text.in_(available_system))
async def sys_chosen(message: types.Message, state: FSMContext):
    await state.update_data(system=message.text)
    await message.answer(
        text="Выберите качество камер",
        reply_markup=make_row_keyboard(available_quality)
    )
    await state.set_state(ChoiceProfile.quality)

@router.message(ChoiceProfile.quality, F.text.in_(available_quality))
async def quality_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await state.update_data(quality=message.text)
    await message.answer(
        text="Выберите количество камер. Можете ввести число сами",
        reply_markup=kb3
    )
    await state.update_data(quality=message.text)
    await state.set_state(ChoiceProfile.count)

@router.message(ChoiceProfile.count)
async def count_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_input = message.text.strip()
    if not user_input.isdigit():  # Проверяем, что введено только число
        await message.answer("Пожалуйста, введите только цифры.")
        return
    user_data = await state.get_data()
    await state.update_data(count=message.text)
    await message.answer(
        f"Ваша система: {user_data['system']}\n"
        f"Качество камер: {user_data['quality']}\n"
        f"Количество камер: {message.text}\n",
        reply_markup=kb1

    )
    await state.clear()

# Блок ввода неправильных значений
@router.message(ChoiceProfile.sys)
async def sys_chosen_incorrect(message: types.Message):
    await message.answer(
        text="Выберите видеосистему",
        reply_markup=make_row_keyboard(available_system)
    )

@router.message(ChoiceProfile.quality)
async def quality_chosen_incorrect(message: types.Message):
    await message.answer(
        text="Выберите качество камер",
        reply_markup=make_row_keyboard(available_quality)
    )

@router.message(ChoiceProfile.count)
async def count_chosen_incorrect(message: types.Message):
    await message.answer(
        text="Выберите количество камер. Можете ввести число сами",
        reply_markup=kb3
    )