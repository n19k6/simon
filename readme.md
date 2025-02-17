Musikbox

- has two modes: dice and motivational quotes
- three small videos are available in 30_video folder
  
  [![phototransistor](/30_video/IMG_5499.png)](https://raw.githubusercontent.com/n19k6/simon/main/30_video/IMG_5499.mp4)

  [![phototransistor](/30_video/IMG_5500.png)](https://raw.githubusercontent.com/n19k6/simon/main/30_video/IMG_5500.mp4)

  [![phototransistor](/30_video/IMG_5504.png)](https://raw.githubusercontent.com/n19k6/simon/main/30_video/IMG_5504.mp4)

- download mp3 for dice numbers 1,2,3,4,5,6 and quotes in mp3 format (e.g. https://ttsmp3.com/ai)
- save files and store them on a micro sd card (rename files and directories according dfplayer mini conventions)
```
#C:\...\DATA                     SD Card
#├───dice                        ├───02
#│       dice_1_de.mp3           │     001.mp3 
#│       dice_2_de.mp3           │     002.mp3 
#│       dice_3_de.mp3           │     003.mp3 
#│       dice_4_de.mp3           │     004.mp3 
#│       dice_5_de.mp3           │     005.mp3 
#│       dice_6_de.mp3           │     006.mp3 
#│                               │
#└───motivation                  └───01
#        motivation_1_de.mp3           001.mp3 
#        motivation_2_de.mp3           002.mp3 
#        motivation_3_de.mp3           003.mp3 
#        motivation_4_de.mp3           004.mp3 
#        motivation_5_de.mp3           005.mp3 
#        motivation_6_de.mp3           006.mp3 
#        motivation_7_de.mp3           007.mp3 
```
- wire components (musikbox_v1_bb.png)
  ![fritzing diagram](/20_musikbox/musikbox_v1_bb.png)
- install micropython onto pico 2 W
- save picodfplayer.py onto pico 2 W
- save test6.py as main.py onto pico 2 W
