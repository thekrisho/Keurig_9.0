# Keurig_9.0 (Tested on CHIP, transferable to Rpi)

Have you ever wanted to hack your Keurig 2.0? Ever wanted coffee ready when you wake up? Take your existing Keurig 2.0 machine, interface with two IOs on a raspberry pi or microcontroller of your choice and make it happen! 

Hardware modification instructions coming soon on Instructables!

Concept: 
The Keurig begins to brew as soon as the handle is lifted, a k-cup is inserted, the handle is closed and the k-cup is recognized. The Keurig then prompts to start by pressing the button. After around a minute if you have not pressed the button, the Keurig times out and requires the handle to be lfited and closed again before prompting brew by pressing button. The objective is to automate this step so you can have coffee brewed at work before you arrive or even sync the timer to your alarm clock on your phone for a quick morning kickstart. 

Hardware Modifications: 
- Access Keurig "handle" sensor and relay to digital I/O
- Access Keurig "Button" sensor and relay to digital I/O

Software:
- Python (Flask) based webserver for web access (with authentication)
- Port Tunnel to avoid exposing localhost (ngrok, pagekite, or openport)


Before you start: 
- Install Python3 with Flask
- Install openport
- Install required GPIO library to work in python (for CHIP: https://github.com/xtacocorex/CHIP_IO)


app.py
- Python (Flask) code to create server which calls brew.py

brew.py
- I/O relay sequence to activate a brew on the Keurig



Im new here, be nice pls XD
