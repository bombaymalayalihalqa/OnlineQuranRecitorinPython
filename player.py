#!/usr/bin/python3
import time
import vlc
def Sound(sound):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(sound)
    player.set_media(media)
    player.play()
    time.sleep(3)
    duration = player.get_length() / 1000
    time.sleep(duration)
a=int(input("Enter Sura number ="))
b=int(input("Enter Aya number  ="))
surasize=[7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6]
if(b>surasize[a-1]):
    print("This sura has only",surasize[a-1], "Ayaths")
else:
    k="https://verses.quran.com/Shuraym/ogg/"+str(a).zfill(3)+str(b).zfill(3)+".ogg"
    Sound(k)

