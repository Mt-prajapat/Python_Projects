import os
import shutil
import datetime

import schedule
import time

source_dir = "C:/Users/moti/Downloads"
destination_dir = "C:Users/moti/Bin"

def copy_folder_to_directory(source, dest):
  today = datetime.date.today()
  dest_dir = os.path.join(dest,str(today))
  
  try:
    shutil.copytree(source,dest_dir)
    print(f"Folder copied to: {dest_dir}")
    
  except Exception as e:
    print(f"Folder already exits in: {dest}")
  
  
schedule.every().day.at("11:13").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
  schedule.run_pending()
  time.sleep(60)