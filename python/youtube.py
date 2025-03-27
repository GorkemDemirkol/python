import yt_dlp  
import tkinter as tk  
from tkinter import filedialog  
from tkinter import messagebox  


def download(url, save_path):  
    try:  
        ydl_opts = {  
            'format': 'best',  # En iyi video ve ses akışını al  
            'outtmpl': f'{save_path}/%(title)s.%(ext)s' # Çıktı dosya adı   
            } 
        

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:  
            ydl.download([url])  
            print("İndirme başarılı!")  

    except Exception as e:  
        print(f"Hata: {e}")  
        messagebox.showerror("Hata", str(e))  


def open_file_dialog():  
    folder = filedialog.askdirectory()  
    if folder:  
        print(f"Seçilen klasör: {folder}")  
        return folder  
    else:  
        print("Klasör seçilmedi.")  
        messagebox.showwarning("Uyarı", "Klasör seçilmedi.")  
        return None  


if __name__ == "__main__":  
    root = tk.Tk()  
    root.title("YouTube Video İndirici")  # Pencere başlığı  
    root.geometry("300x150")  # Pencere boyutu  
    root.withdraw()  # Ana pencereyi gizle  

    video_url = input("Video URL'sini girin: ")  
    save_fold = open_file_dialog()  

    if save_fold:  
        download(video_url, save_fold)  
    else:  
        print("İşlem iptal edildi.")  