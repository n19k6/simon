Musikbox

- has two modes: dice and motivational quotes
- three small videos are available in 30_video folder
- download mp3 for dice numbers 1,2,3,4,5,6 and quotes in mp3 format (e.g. https://ttsmp3.com/ai)
- save files and store them on a micro sd card (rename files and directories according dfplayer mini conventions)
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
- wire components (musikbox_v1_bb.png)
- install micropython onto pico 2 W
- save picodfplayer.py onto pico 2 W
- save test6.py as main.py onto pico 2 W




















BACKUP:

projects:
- dice
- simon game
- iot led

specific:
- laptops 6+1 (internet connection, usb serial and usb mass storage has to be enabled)
- create 6 accounts (byom, wokwi)
- 2h time

remarks:
wokwi (gd.2005@/#b.e)
thonny

sources:
https://ttsmp3.com/text-to-speech/German/
https://www.elektronik-kompendium.de/sites/raspberry-pi/2612221.htm
https://www.upesy.com/blogs/tutorials/timer-raspberry-pi-pico-with-micropython?srsltid=AfmBOopKQJ6kwD6BWrbn1F_ckJz1IxxKU3RhbEfUu0BstRFCzXih0swc



https://blog.cleverly.de/motivationssprueche-lernen/#penci-Motivierende-Zitate-und-Sprueche-fuer-erfolgreiches-Lernen
"Die Entfernung ist unwichtig. Nur der erste Schritt ist wichtig."
~ Marquise du Deffand
"Es ist immer zu früh, um aufzugeben."
~ Norman Vincent Peale
"Niemand weiß, was er kann, bis er es probiert hat"
~ Publilius Syrus
„Es gibt zwei Arten, sein Leben zu leben: entweder so, als wäre nichts ein Wunder, oder so, als wäre alles ein Wunder."
~ Albert Einstein
„Probleme kann man niemals mit derselben Denkweise lösen, durch die sie entstanden sind."
~ Albert Einstein
„Wer einen Fehler gemacht hat und ihn nicht korrigiert, begeht einen zweiten."
~ Konfuzius
"Alle Träume können wahr werden, wenn wir den Mut haben ihnen zu folgen."
~ Walt Disney

update:
1. dice (press button, say 1-6, trigger via callback)
2. musikbox (light and button, trigger motivational cite)

discarded:
- speeking clock
