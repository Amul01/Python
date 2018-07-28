from pytube import YouTube

link=input("Enter the video link: ")
loc=input("Enter the storage location: ")

yt = YouTube(link)
yt.streams.first().download(loc)
