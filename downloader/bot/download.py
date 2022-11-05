from django.conf import settings
from telebot import TeleBot
from pytube import YouTube

import os

def download_video(call_data):
    call = call_data.split("/")
    url = "https://www.youtube.com/watch?v=" + call[1]
    resolution = call[2]
    yt = YouTube(url=url)
    st = yt.streams.filter(file_extension='mp4', type="video", resolution=resolution)
    file = st.first().download(settings.MEDIA_URL)
    return file

def download_audio(call_data):
    call = call_data.split("/")
    url = "https://www.youtube.com/watch?v=" + call[1]
    yt = YouTube(url=url)
    st = yt.streams.filter(type='audio')
    file = st.first().download(settings.MEDIA_URL)
    base, exp = os.path.splitext(file)
    new_file = base + '.mp3'
    os.rename(file, new_file)
    return new_file
