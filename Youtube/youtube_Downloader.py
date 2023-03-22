from pytube import YouTube

link = "https://www.youtube.com/watch?v=6ZwwapPikyQ&ab_channel=MLRecords"
youtube_1 = YouTube(link)
# Title = youtube_1.title
# Thumb = youtube_1.thumbnail_url
# print(Title, "\n", Thumb)

# videos = youtube_1.streams.all()

# videos = youtube_1.streams.filter(only_audio=True)
 
vid_list = list(enumerate(videos))
for i in vid_list:
    print(i)
print()
strm = int(input("Enter :"))
videos[strm].download()
print("Ho gaya ree!!")
