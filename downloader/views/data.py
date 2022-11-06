import pafy


def get_resolutions(streams):
    st = streams.filter(progressive=True, file_extension='mp4', type="video")
    resolutions = []
    for vid in st:
        if vid.resolution not in resolutions:
            resolutions.append(vid.resolution)
    return resolutions

def video_data(url):
    video = pafy.new(url)
    video_id = video.videoid
    link = "https://www.youtube.com/embed/" + video_id
    title = video.title
    author = video.author

    data = {
        "yt_player": link ,
        "title": title,
        "author": author,
        "id": video_id,
    }

    return data