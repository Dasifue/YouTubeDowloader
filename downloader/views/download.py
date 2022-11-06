from django.shortcuts import redirect
from django.urls import reverse_lazy

from pytube import YouTube

import os


def download_video(request, video_id, resolution):
    url = "https://www.youtube.com/watch?v=" + video_id
    yt = YouTube(url)
    st = yt.streams.filter(file_extension='mp4', type="video", resolution=resolution)
    st.first().download()
    return redirect(reverse_lazy("videos"))


def download_audio(request, video_id):
    url = "https://www.youtube.com/watch?v=" + video_id
    yt = YouTube(url)
    st = yt.streams.filter(type='audio')
    file = st.first().download()
    base, exp = os.path.splitext(file)
    new_file = base + '.mp3'
    os.rename(file, new_file)
    return redirect(reverse_lazy("videos"))