from os import remove,system
system("pip install pytube")
system("pip install requests")
from pytube import YouTube,Channel,Playlist# pip install pytube
from requests import post #pip install requests
from time import sleep
import datetime,json

__author__ = "Ahmed Jo"
__version__ = "1.0.1"

FILENAME = "queue.txt"

with open(FILENAME,"a") as Links :
    Links.write(f"\n\n------{datetime.datetime.now()}------: \n\n")


key = "EAAQSADNAVzYBAAEeBmPQlfABFtLE2mI3at1oiJ2T0RyAD1PYLGB4EYrXSrPm9FqTREpbjfcrGjZA28L9xlBKRpLfiZAUB1Jlu2abHCaGv4tDHV6hOIEJ10ZCkt4R6gnYW0W3SfExCNizJTDR8OhUWZAViJBEZBIGukRJqnSguo3tZCZCWNTzIYy"
links = Playlist("https://youtube.com/playlist?list=PLfoWGnXmx4miKngyOPZGpQS3FIX9sufxK")

for i in links:
    try :
        VIDEOO = YouTube(i)
        if ((VIDEOO.length)/60)<150:
            U = VIDEOO.streams.filter(progressive=True,res="720p")
            if len(U)==0:
                U = VIDEOO.streams.filter(progressive=True,res="480p")
                if len(U)==0:
                    U = VIDEOO.streams.filter(progressive=True,res="360p")
            if len(U)==0:
                U = VIDEOO.streams.filter(res="720p")
                if len(U)==0:
                    U = VIDEOO.streams.filter(res="480p")
                    if len(U)==0:
                        U = VIDEOO.streams.filter(res="360p")
            print(f"Start Download {i}")
            VID = U[0].download(filename="current_video.mp4")
            print(f"{i} Is Successfully Downloaded")
            vid = VIDEOO
    except :
        print(f"ERROR : while Downloading {i} ")
    else :
        TITLE = f"""
🖋 : {vid.title}
👤 : {vid.author}
👁‍🗨 : {vid.views}
🗓️ : {vid.publish_date}
↗️️ : {vid.watch_url}


POSTED IN {datetime.datetime.now()} BY OUR BOT.
"""
        url = "https://graph-video.facebook.com/v13.0/me/videos"
        #        ffmpeg -i namevi -vcodec h264 -acodec aac _newnamevi
        print("start compression the video ")
        system(f"ffmpeg -i current_video.mp4 -vcodec h264 -acodec aac new_current_video.mp4")
        files = {"source": open("new_current_video.mp4", "rb")}
        payload = {
        "access_token": key,
        "title": vid.title,
        "description": TITLE
    }
        print("start uploading")
        try:
            #Try To upload Video
            res = post(url, files=files, data=payload)
        except:

            # Signal if publication fails
            print(f"{datetime.datetime.now()}    Upload Failed")

        else:
            print(res.text)
            # get uploaded post from response
            post_id = json.loads(res.text).get("id")
                
            # generate Link of uploaded Post
            link = f"https://www.facebook.com/101008699261867/videos/{post_id}"
                
            # save post info
            with open(FILENAME, "a") as b:
                b.write(f"""\n{vid.title} :\n{link}\n""")
            #https://www.facebook.com/101008699261867/posts/122202933809110/?app=fbl
            # Signal if the post is published
            print(f"{datetime.datetime.now()}    Upload Successfully {link}")
            remove("current_video.mp4")
            remove("new_current_video.mp4")
        sleep(10*60)

print(f"☑ Upload Finish, check {FILENAME} To get your uploaded posts.")#### pip install PyOpenGL PyOpenGL_accelerate
