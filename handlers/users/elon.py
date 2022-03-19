from aiogram import types
from data.config import CHANNELS
# from data.config import CHANNELS
from states.state import Elon
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from keyboards.default.knopka import menu
from keyboards.inline.buton import sendd
from keyboards.inline.admin_con import send_ad
from loader import dp


@dp.message_handler(text = "E'lon berish")
async def dfda(message:types.Message):
    await message.answer("Mahsulot nomini kiriting")
    await Elon.name.set()

@dp.message_handler(state= Elon.name)
async def ismf(message:types.Message,state:FSMContext):
    name = message.text
    await state.update_data(
        {'name': name}
    )
    await message.answer("Mahsulot haqida to'liq ma'lumot kiriting")
    await Elon.next()

@dp.message_handler(state= Elon.f_name)
async def isf(message:types.Message,state:FSMContext):
    f_name = message.text
    await state.update_data(
        {'f_name': f_name}
    )
    await message.answer("Mahsulot narxini kiriting")
    await Elon.next()

@dp.message_handler(state= Elon.price)
async def iscf(message:types.Message,state:FSMContext):
    price = message.text
    await state.update_data(
        {'price': price}
    )
    await message.answer("Telefon raqamingizni kiriting")
    await Elon.next()


@dp.message_handler(state= Elon.phone)
async def iscf(message:types.Message,state:FSMContext):
    phone = message.text
    await state.update_data(
        {'phone': phone}
    )
    await message.answer("Manzilingizni kiriting")
    await Elon.next()

@dp.message_handler(state= Elon.loc)
async def iscf(message:types.Message,state:FSMContext):
    loc = message.text
    await state.update_data(
        {'loc': loc}
    )
    await message.answer("Mahsulot rasmini yuboring")
    await Elon.next()


@dp.message_handler(content_types=['photo'],state = Elon.photo)
async def tit(message:types.Message,state:FSMContext):
    photo = message.photo[-1].file_id

    await state.update_data(
        {'photo':photo}
    )
    data = await state.get_data()
    name = data.get('name')
    f_name = data.get('f_name')
    price = data.get('price')
    phone = data.get('phone')
    loc = data.get('loc')
    phot = data.get('photo')
    await message.answer_photo(photo = phot, caption = f"Mahsulot nomi: {name}\nMahsulot haqida: {f_name}\nMahsulot narxi: {price}\nTel raqam: {phone}\nManzil: {loc}",reply_markup=sendd)
    await Elon.next()

@dp.callback_query_handler(text = 'tasq',state=Elon.send)
async def dd(call:types.CallbackQuery,state:FSMContext):
    data = await state.get_data()
    name = data.get('name')
    f_name = data.get('f_name')
    price = data.get('price')
    phone = data.get('phone')
    loc = data.get('loc')
    phot = data.get('photo')
    # await message.answer("Adminga jo'natildi",show_alert = True)
    await call.bot.send_photo(5012333108,photo = phot, caption = f"Mahsulot nomi: {name}\nMahsulot haqida: {f_name}\nMahsulot narxi: {price}\nTel raqam: {phone}\nManzil: {loc}",reply_markup=send_ad)
    await call.answer("Adminga jo'natildi",show_alert=True)
    await call.message.edit_reply_markup()
    await state.finish()

@dp.callback_query_handler(text ='non',state=Elon.send)
async def hh(call:types.CallbackQuery,state:FSMContext):
    # await call.message.answer("Qabul qilinmadi")
    await call.message.delete()
    await call.message.answer("Bekor qilindi",reply_markup=menu)
    await state.finish()

@dp.callback_query_handler(text='send_ch')
async def ad_send(call:types.CallbackQuery):
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=CHANNELS[0])


@dp.callback_query_handler(text='send_ch')
async def ad_send(call:types.CallbackQuery):
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=CHANNELS[0])

