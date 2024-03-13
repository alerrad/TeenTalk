from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from ..lexicon import LEXICON_RU


commands_router = Router()


@commands_router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@commands_router.message(Command(commands='feedback'))
async def leave_feedback(message: Message):
    await message.answer(text=LEXICON_RU['/feedback'])
