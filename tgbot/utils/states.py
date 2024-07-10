from aiogram.fsm.state import State, StatesGroup


class TestState(StatesGroup):
    text = State()
