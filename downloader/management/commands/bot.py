from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot

from downloader.bot.delete import delete_file
from downloader.bot.download import download_video, download_audio
from downloader.bot.get_data import get_videos

bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    text = "Hello, nice to see you there. Path YouTube video link"
    bot.send_message(message.chat.id, text, reply_markup=None)
    bot.register_next_step_handler(message=message, callback=get_videos)
    text = "It will take some time. Please, be patient"
    bot.send_message(message.chat.id, text=text, reply_markup=None)

@bot.message_handler(commands=['new_link'])
def send_welcome_message(message):
    text = "Path YouTube video link"
    bot.send_message(message.chat.id, text, reply_markup=None)
    bot.register_next_step_handler(message=message, callback=get_videos)

@bot.message_handler(commands=['start'])
def new_request(message):
    text = "Something new? Share me the link"
    bot.send_message(message.chat.id, text, reply_markup=None)
    bot.register_next_step_handler(message=message, callback=get_videos)



@bot.callback_query_handler(func=lambda call: str(call.data)[:5] in ("video", "audio"))
def download(call):
    try:
        message = call.message
        data = str(call.data)[:5]
        if data == "video":
            file = download_video(call_data=call.data)
            bot.send_document(message.chat.id, document=open(file, "rb"))
        elif data == "audio":
            file = download_audio(call_data=call.data)
            bot.send_document(chat_id=message.chat.id, document=open(file, "rb"))
        delete_file(file)
        text = "Here it is! To send new link again send /new_link command."
        bot.send_message(message.chat.id, text=text, reply_markup=None)
    except:
        text = "Error! Something went wrong. Try again leter"
        bot.send_message(message.chat.id, text=text, reply_markup=None)


class Command(BaseCommand):

    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()								
        bot.infinity_polling()			