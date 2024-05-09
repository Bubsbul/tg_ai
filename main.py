from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '7022740450:AAG7rR_O6PeehnkE0rBddPxPWx6aGFapMW0'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)

async def send_echo_photo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

async def send_echo_sticker(message: Message):
    await message.reply_sticker(message.sticker.file_id)

dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_echo_photo, F.content_type == ContentType.PHOTO)
dp.message.register(send_echo_sticker, F.content_type == ContentType.STICKER)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
