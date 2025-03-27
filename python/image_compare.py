import cv2
def compare_images(image1,image2):
    #sisteme resimleri okutuk
    image1 = cv2.imread(image1)
    image2 = cv2.imread(image2)
    #resimler doğru yüklenmiş mi kontrol ediyoruz
    if image1 is None or image2 is None:
        print("Resimler yüklenemedi")
        return
    #resilerin boyutlarını eşitleme
    image1 = cv2.resize(image1,(500,500))
    image2 = cv2.resize(image2,(500,500))
    #iki resim arasındaki farkı bulma
    difference=cv2.subtract(image1,image2)
    r,g,b=cv2.split(difference)
    #iki resim arasında fark yoksa rgb 0 gelecedğinden siyah olur
    if cv2.countNonZero(r)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(b)==0:
        print("bu iki resim tıpatıp aynı")
    else:
        #maskeleme işlemi iki resim arasındaki farkı beyaz yapar
        conv_hsv=cv2.cvtColor(difference,cv2.COLOR_BGR2GRAY)
        red,mask=cv2.threshold(conv_hsv,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

        difference[mask!=255]=[0,0,255]
        image1[mask!=255]=[0,0,255]
        image2[mask!=255]=[0,0,255]
        diff="difference.png"
        cv2.imwrite(diff,difference)
        print("Resimler birbirinden farklı")
image_path1="image3.jpg"
image_path2="image2.jpg"
compare_images(image_path1,image_path2)