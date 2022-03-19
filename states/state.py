from aiogram.dispatcher.filters.state import State,StatesGroup

class Elon(StatesGroup):
    name = State()
    f_name = State()
    price = State()
    phone = State()
    loc = State()
    photo = State()
    send = State()