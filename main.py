from math import *
from aiogram.types import Message
from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling
from aiogram.utils.exceptions import MessageTextIsEmpty


API_TOKEN = "API_TOKEN"
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def Start(msg: Message):

    await msg.answer("Добро пожаловать в калькулятор!")
    await msg.answer("Введите комманду /help для получения справки о калькуляторе")
    await msg.answer("Пример взаимодействия:\nВвод: 5 + 7\nВывод: 12")


@dp.message_handler(commands="help")
async def Help(msg: Message):

    await msg.answer("Данный телеграм-бот принимает выражение и возвращает результат, работает как калькулятор")
    await msg.answer("Математические операторы:\n+ - сложение\n- - вычитание (унарный минус)\n* - умножение\n** - возведение в степень\n/ - деление\n// - непосредственное целочисленное деление\n% - остаток от деления")
    await msg.answer("Математические функции:\nsqrt(num) - квадратный корень от числа num\npow(a, b) - возведение числа a в степень b\npi - число π\ne - число e\nfactorial(x) - факториал числа x\nround(x) - округление числа x")
    await msg.answer("Логические операторы:\n== - равно\n!= - не равно\n> - больше\n< - меньше\n>= - больше или равно\n<= - меньше или равно\nand - И\nor - ИЛИ\nnot - НЕ\n\nTrue - Правда\nFalse - Ложь")


@dp.message_handler()
async def Solver(msg: Message):

    try:
        if isinstance(eval(msg.text), int) or isinstance(eval(msg.text), float) or isinstance(eval(msg.text), bool):
            if isinstance(eval(msg.text), float) and eval(msg.text) - int(eval(msg.text)) == 0.0:
                await msg.answer(int(eval(msg.text)))
            else:
                await msg.answer(eval(msg.text))
        else:
            raise NameError
    except ArithmeticError:
        await msg.answer("Произошла ошибка при вычислении!")
        await msg.answer("Попробуйте ввести другой пример.")
    except (NameError, SyntaxError, ValueError, TypeError):
        await msg.answer("Неверный тип ввода!")
        await msg.answer("Попробуйте ввести другой пример.")
    except MessageTextIsEmpty:
        await msg.answer("Неверный тип ввода!")
        await msg.answer("Попробуйте ввести другой пример.")


start_polling(dp, skip_updates=True)
