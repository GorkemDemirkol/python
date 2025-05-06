import glob
import tkinter as tk
from tkinter import *
import vlc

def last(list):
    return list[-1]


def music_name():
    global my_music,music_number
    return last(my_music[music_number].split("/"))


def play_music():
    global music_number,my_music,player,instance
    to_play=my_music[music_number]
    media=instance,media_new(to_play)
    player.set_media(media)
    player.pygame.music.play()


def pause_music():
    player.pause()


def next_music():
    global music_number,my_music,music_label
    if music_number>0:
        music_number-=1
    music_label.config(text=str(music_name()))
    
music_number=0
window=tk()
window.geometry("300x200")
window.resizable(0,0)
window.title("Mp3 Player")

instance=vlc.Instance()
player=instance.media_player_new()

my_music=glob.glob("*.mp3")

play_image=PhotoImage(file="play.png")
pause_image=PhotoImage(file="pause.png")
forwerd_image=PhotoImage(file="forwerd.png")
previous_image=PhotoImage(file="previous.png")
stop_image=PhotoImage(file="stop.png")

music_label=tk.Label(window,text=music_name())

play=tk.Button(window,image=play_image,command=play_music)
pause=tk.Button(window,image=pause_image,command=pause_music)
forwerd=tk.Button(window,image=forwerd_image,command=next_music)
previous=tk.Button(window,image=previous_image,command=previous_music)
stop=tk.Button(window,image=stop_image,command=n)

music