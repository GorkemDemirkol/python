import os
import shutil
import datetime
import schedule
import time

source_folder=r"C:\Users\d-e-m\Desktop\blogsite"
destination_folder=r"C:\Users\d-e-m\Desktop\backUp"

def copy_folder_to_directory(source,dest):
    today=datetime.date.today()
    dest_dir=os.path.join(dest,str(today))

    try:
        shutil.copytree(source,dest_dir)
        print(f"{source} klasörü {dest_dir} klasörüne başarıyla kopyalandı.")
    except FileExistsError:
        print(f"{dest_dir} klasörü zaten var.")
        pass

schedule.every().day.at("22:04").do(lambda:copy_folder_to_directory(source_folder,destination_folder))

while True:
    schedule.run_pending()
    time.sleep(30)