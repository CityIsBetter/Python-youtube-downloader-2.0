from tkinter import *
import customtkinter
from pytube import YouTube
from pathlib import Path

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Python Youtube Downloader")
title = customtkinter.CTkLabel(master=root,text="Youtube Video Downloader",font=('geneva',30))
title.place(x=80,y=50)
link = customtkinter.CTkEntry(master=root, placeholder_text="Paste your url here",width=300)
link.place(x=100,y=120)

def downM():
    path = str(Path.home()/ 'Downloads')
    url = YouTube(str(link.get()))
    name = url.title
    name = name.replace('\\', '').replace('/', '')
    new_name = f'{name}.mp3'
    video = url.streams.get_audio_only()
    video.download(output_path=f'{path}',filename=new_name)
    Label(root,text="Downloaded Music",font="arial 15 bold").place(x=200,y=250)

def downV():
    path = str(Path.home()/ 'Downloads')
    url = YouTube(str(link.get()))
    name = url.title
    name = name.replace('\\', '').replace('/', '')
    new_name = f'{name}.mp4'
    video = url.streams.get_highest_resolution()
    video.download(output_path=f'{path}',filename=new_name)
    Label(root,text="Downloaded Video",font="arial 15 bold").place(x=200,y=250)
        
buttonM = customtkinter.CTkButton(master=root, text="Download Music", command=downM,height=50)
buttonM.place(x=275,y=200)
buttonV = customtkinter.CTkButton(master=root, text="Download Video", command=downV,height=50)
buttonV.place(x=80,y=200)
root.mainloop()

