from django.conf import settings
from telebot import TeleBot
from pytube import YouTube

import pafy

from telebot.types import (

    InlineKeyboardMarkup,
    InlineKeyboardButton,

)

bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)

def get_videos(message):
    text = "It will take some time. Please, be patient. Карина не души"
    bot.send_message(message.chat.id, text=text, reply_markup=None)
    url = message.text
    markup = InlineKeyboardMarkup()
    yt = YouTube(url)
    streams = yt.streams
    video = pafy.new(url)
    video_id = video.videoid
    resolutions = get_resolutions(streams=streams)

    for res in resolutions:
        btn = InlineKeyboardButton(res, callback_data=f"video/{video_id}/{res}")
        markup.add(btn)
    
    audio = InlineKeyboardButton("audio", callback_data=f"audio/{video_id}")
    markup.add(audio)
    text = "Good. Now select video quality or just audio"
    bot.send_message(message.chat.id, text=text, reply_markup=markup)


def get_resolutions(streams):
    st = streams.filter(progressive=True, file_extension='mp4', type="video")
    resolutions = []
    for vid in st:
        if vid.resolution not in resolutions:
            resolutions.append(vid.resolution)
    return resolutions