from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from pytube import YouTube

from .forms import VideoURLForm

import os

url = ""

def get_resolutions(streams):
    st = streams.filter(progressive=True, file_extension='mp4', type="video")
    resolutions = []
    for vid in st:
        if vid.resolution not in resolutions:
            resolutions.append(vid.resolution)
    return resolutions


def videos_list(request):
    form = VideoURLForm()
    global url
    if request.method == "POST":
        form = VideoURLForm(request.POST)
        if form.is_valid():
            url = request.POST.get("url")
            yt = YouTube(url)
            streams = yt.streams
            resolutions = get_resolutions(streams=streams)

            context = {
                "url": url,
                "form": form,
                "resolutions": resolutions,
                "audio": "audio"
            }

        return render(request=request, template_name="download.html", context=context)
    return render(request=request, template_name="download.html", context={"form": form})


def download_video(request, resolution):
    global url
    yt = YouTube(url)
    st = yt.streams.filter(file_extension='mp4', type="video", resolution=resolution)
    st.first().download()
    return redirect(reverse_lazy("videos"))


def download_audio(request):
    yt = YouTube(url)
    st = yt.streams.filter(type='audio')
    file = st.first().download()
    base, exp = os.path.splitext(file)
    new_file = base + '.mp3'
    os.rename(file, new_file)
    return redirect(reverse_lazy("videos"))
