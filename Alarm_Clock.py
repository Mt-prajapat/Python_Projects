from playsound import playsound
import time

Clear = "\033[2J"
Clear_And_Return = "\033[H"
def alarm(seconds):
  time_elapsed = 0
  
  print(Clear)
  
  while time_elapsed < seconds:
    time.sleep(1)
    time_elapsed += 1
    
    time_left = seconds - time_elapsed
    minutes_left = time_left // 60
    seconds_left = time_left % 60
    
    print(f"{Clear_And_Return}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    
  playsound("Din_Main_toh_Dhunde_police_viral_trending_song_48KBPS.mp4")
  
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_time = minutes * 60 + seconds
alarm(total_time)
    
