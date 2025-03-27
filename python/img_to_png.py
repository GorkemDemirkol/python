import os
import img2pdf
def images_to_pdf(imgs_path):
    #resimleri pdf e çevirme
    if os.path.exists(imgs_path):
        print("Resimler bulundu")
    else:
        print("Resimler bulunamadı")
        return
    images=[imgs for imgs in os.listdir(imgs_path) if imgs.endswith(("jpg","png","jpeg"))]
    images.sort()

    images_bytes=list()

    for i in images:
        with open(os.path.join(imgs_path,i),"rb") as file:
            images_bytes.append(file.read())
    pdf_img_bytes=img2pdf.convert(images_bytes)
    with open("pdf.pdf","wb") as file:
        file.write(pdf_img_bytes)

img_folder_path="image"
images_to_pdf(img_folder_path)
