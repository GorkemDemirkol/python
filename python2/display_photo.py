import os
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

class PhotoViewer:
    def __init__(self,root,photo_folder):
        self.root=root
        self.root.title("Fotoğraf Görüntüleyici")
        self.photo_folder=photo_folder
        self.photos=[f for f in os.listdir(photo_folder)if f.endswith(('.png','.jpg','.jpeg','.gif','.webp'))]
        self.current_index=0

        self.image_label=Label(self.root)
        self.image_label.pack()

        self.prev_button=Button(self.root,text="Önceki",command=self.show_prev_photo)
        self.prev_button.pack(side=LEFT,padx=10)

        self.delete_button = Button(self.root, text="Sil", command=self.delete_photo)  # Düzeltildi  
        self.delete_button.pack(side=LEFT, padx=380)  

        self.next_button=Button(self.root,text="Sonraki",command=self.show_next_photo)
        self.next_button.pack(side=RIGHT,padx=10)
        self.show_photo()  
    def show_photo(self):
        if not self.photos:
            messagebox.showinfo("Bilgi","Fotoğraf yok.")
            return

        photo_path=os.path.join(self.photo_folder,self.photos[self.current_index])
        image=Image.open(photo_path)
        image.resize((800,600),Image.Resampling.LANCZOS)
        self.photo=ImageTk.PhotoImage(image)

        self.image_label.config(image=self.photo)
        self.image_label.image=self.photo  

    def show_next_photo(self):
        if not self.photos:
            return
        self.current_index=(self.current_index+1)%len(self.photos)
        self.show_photo()
    def show_prev_photo(self):
        if not self.photos:
            return
        self.current_index=(self.current_index-1)%len(self.photos)
        self.show_photo()
    def delete_photo(self):
        if not self.photos:
            messagebox.showwarning("Uyarı","Silinecek fotoğraf yok.")
            return
        photo_path=os.path.join(self.photo_folder,self.photos[self.current_index])
        os.remowe(photo_path)
        del self.photos[self.current_index]
        if self.photos:
            self.current_index%len(self.photos)
        else:
            self.image_label.config(image=None)
            messagebox.showinfo("Bilgi","Tüm fotoğraflar silindi.")
            return
        self.show_photo()
        

if __name__=="__main__":
    root=Tk()
    photo_folder=r"C:/Users/d-e-m/Desktop/python/image"
    viewer=PhotoViewer(root,photo_folder)
    root.mainloop()
        