from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=YWIRmrVbNt4")
yt.set_filename("Soul Reflections Ep1")
mp4files = yt.filter('mp4')
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
d_video.download('/F/BKShivani')
