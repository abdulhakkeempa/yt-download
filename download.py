from pytube import YouTube

#where to save
SAVE_PATH = "downloads" #to_do

#link of the video to be downloaded

link=[
  "https://youtu.be/q2xcxzNiJsc",
	"https://youtu.be/MAIG_L8vkE4",
  "https://youtu.be/ENeL5mlOrG0",
  "https://youtu.be/K2E4atb2IVQ",
  "https://youtu.be/BdQr7JDwMjE", 
  "https://youtu.be/uFkWQr-9aIU", 
  "https://youtu.be/1p0pV69JKrM"
]

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(mime_type="video/mp4",res="720p",progressive="True").first()
    print(youtubeObject)
    try:
        youtubeObject.download(SAVE_PATH)
    except Exception as e:
        print(e)
    print("Download is completed successfully")


for i in link:
  download(i)