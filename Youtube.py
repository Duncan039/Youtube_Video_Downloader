import pytube
from pytube import YouTube
link = input("Enter the Video link of the Video you would like to Download: ")
yt = YouTube(link)
print("Title of the Video:", yt.title)
print("Number of Views: ", yt.views)
download = yt.streams.get_highest_resolution()
yt.download(r"C:\Users\user\Desktop\ADS")
