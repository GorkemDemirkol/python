import glob  
import tkinter as tk  
from tkinter import PhotoImage  
import vlc  

def last(lst):  
    return lst[-1]  

def music_name():  
    global my_music, music_number  
    return last(my_music[music_number].split("/"))  

def play_music():  
    global music_number, my_music, player, instance  
    to_play = my_music[music_number]  
    media = instance.media_new(to_play)  
    player.set_media(media)  
    player.play()  # player.pygame.music.play() kısmını player.play() olarak düzelttim.  

def pause_music():  
    player.pause()  

def next_music():  
    global music_number, my_music, music_label  
    if music_number < len(my_music) - 1:  # Liste sınırlarını aşmamak için.  
        music_number += 1  
    music_label.config(text=music_name())  

def previous_music():  
    global music_number, my_music, music_label  
    if music_number > 0:  
        music_number -= 1  
    music_label.config(text=music_name())  

def stop_music():  
    player.stop()  

# Değişkenleri başlat  
music_number = 0  
window = tk.Tk()  # tk yerine Tk() kullanmayı düzelt.  
window.geometry("300x200")  
window.resizable(0, 0)  
window.title("Mp3 Player")  

instance = vlc.Instance("C:/Program Files/VideoLAN/VLC/libvlc.dll")  
player = instance.media_player_new()  

my_music = glob.glob(r"C:/Users/d-e-m/Desktop/python/Music.mp3")  

# Resimleri yükleme (bu yolların doğru olduğundan emin olun)  
play_image = PhotoImage(file="play.png")  
pause_image = PhotoImage(file="pause.png")  
forward_image = PhotoImage(file="forward.png")  # "forwerd" yerine "forward" olarak düzelttim.  
previous_image = PhotoImage(file="previous.png")  
stop_image = PhotoImage(file="stop.png")  

music_label = tk.Label(window, text=music_name())  
music_label.pack()  

play = tk.Button(window, image=play_image, command=play_music)  
pause = tk.Button(window, image=pause_image, command=pause_music)  
forward = tk.Button(window, image=forward_image, command=next_music)  
previous = tk.Button(window, image=previous_image, command=previous_music)  
stop = tk.Button(window, image=stop_image, command=stop_music)  

play.pack(side=tk.LEFT)  
pause.pack(side=tk.LEFT)  
forward.pack(side=tk.LEFT)  
previous.pack(side=tk.LEFT)  
stop.pack(side=tk.LEFT)  

# GUI döngüsünü başlat  
window.mainloop()  