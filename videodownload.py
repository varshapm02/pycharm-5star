from tkinter import *
from tkinter import filedialog
from pytube import *
from shutil import *
from moviepy import *

root=Tk()

def directory():
    folder_path=filedialog.askdirectory()
    select_label.config(text=folder_path)


def download():
    destpath=select_label.cget("text")
    Youtubeurl = url_path.get()
    video = YouTube(Youtubeurl).streams.get_highest_resolution()
    #updatedvideo=VideoFileClip(video)
    #updatedvideo.close()
    move(video,destpath)
    finalconfirm.config(text="Video is downloaded successfully!!")


canvas=Canvas(root,width=400,height=400)
canvas.pack()


title_label=Label(root,text="Video Downloader",fg="blue")
canvas.create_window(200,15,window=title_label)

url_path=Entry(root,width=30)
canvas.create_window(200,90,window=url_path)

url_label=Label(text="Enter the link here:",font="Arial")
canvas.create_window(200,50,window=url_label)



b=Button(root,text="select",fg="red",command=directory)

canvas.create_window(200,200,window=b)

select_label=Label(root,text="select the path where the video should get downloaded")
canvas.create_window(200,170,window=select_label)


download_button=Button(root,text="Download",fg="olive",command=download)
canvas.create_window(200,260,window=download_button)

finalconfirm=Label(root,text="Video is not yet downloaded!!")
canvas.create_window(200,300,window=finalconfirm)

root.mainloop()

