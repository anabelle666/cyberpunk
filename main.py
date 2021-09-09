from pytube import YouTube
url="https://youtu.be/zOvsyamoEDg"
my_video=YouTube(url)
s=my_video.streams.get_highest_resolution()
s.download()
