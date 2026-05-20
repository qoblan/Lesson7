from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from datas import add_to_db,show_users

class RegState(StatesGroup):
    name = State()
    phone = State()
    adress = State()


admin_id=5955492506
api = ''
bot = Bot(api)
dp=Dispatcher()

@dp.message(Command('start'))
async def send_salem(sms:types.Message):
    if sms.from_user.id==admin_id:
        await sms.answer(text='Salem admin')
    else:
        await sms.answer(text='salem',)
        
@dp.message(F.text=='Registration')
async def start_reg(sms:types.Message,state:FSMContext):
    await sms.answer(text='Напишите своё имя:')
    await state.set_state(RegState.name)
@dp.message(RegState.name)
async def save_name(sms:types.Message,state:FSMContext):
    await state.update_data(ati=sms.text)
    await sms.answer(text='Теперь напишите свой номер телефона:')
    await state.set_state(RegState.phone)
@dp.message(RegState.phone)
async def save_number(sms:types.Messagem,state:FSMContext):
    await state.update_data(nomeri=sms.contact.phone_number)
    await sms.answer(text='Теперь напише свой адресс:')
    await state.set_state(RegState.adress)
@dp.message(RegState.adress)
async def save_adress(sms:types.Message,state:FSMContext):
    await state.update_data(adress=sms.text)
    await sms.answer(text='Спасибо, вы прошли регистрацию:')
    datas = await state.get_data()
    await add_to_db(id=sms.from_user.id,
                    name=datas['ati'],
                    phone=datas['nomeri'],
                    adress=datas['adress'])
    await state.clear()



async def main():
    await dp.start_polling(bot)


if __name__=='main':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())





