from django.shortcuts import render

from pytube import YouTube, exceptions

from ..forms import VideoURLForm

from .data import get_resolutions, video_data

def videos_list(request):
    form = VideoURLForm()
    if request.method == "POST":
        form = VideoURLForm(request.POST)
        if form.is_valid():
            try:
                url = request.POST.get("url")
                yt = YouTube(url)
                streams = yt.streams
                resolutions = get_resolutions(streams=streams)

                context = {
                    "video_data": video_data(url=url),
                    "form": form,
                    "resolutions": resolutions,
                    "audio": "audio"
                }
            
            except exceptions.RegexMatchError:

                return render(request, "error.html")

        return render(request=request, template_name="download.html", context=context)
    return render(request=request, template_name="download.html", context={"form": form})