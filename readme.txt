### Journal ###
After the first 2 days almost everything is ready, except for the audio 
 (I didn't figure out how to count the system sound,
 I only managed to record the sound from the microphone, 
 but I have to go and how to fix it)

 Method of fixing  - stereo mixer as default

 3rd day - stuck on recording a video to a file (it plays very quickly when launched)
 Everything else is ready.

 Method of fixing - less FPS 


###Links used in the process ###

https://www.thepythoncode.com/article/make-screen-recorder-python
https://www.thepythoncode.com/article/play-and-record-audio-sound-in-python
https://www.thepythoncode.com/article/download-web-page-images-python
https://www.youtube.com/watch?v=1RE5tSPO2RI&ab_channel=TheCodex (GUI Automation with
PyAutoGUI)
https://stackoverflow.com/questions/48975874/how-record-the-screen-while-selenium-python-is-running-windows-10/48988268
https://www.youtube.com/watch?v=Xjv1sY630Uc&ab_channel=TechWithTim (Web Scraping, Bots &
Testing)
https://python-sounddevice.readthedocs.io/en/0.4.1/usage.html#recording
https://www.youtube.com/watch?v=1eHQIu4r0Bc&ab_channel=CodingEntrepreneurs (Record Video in
OpenCV & Python)
https://stackoverflow.com/questions/66138578/convert-waves-to-decibels-in-python ( Convert waves to decibels )


### RUN ###
	To run the script, you may have the downloaded python v.3.5+
     (if you don't have any, download it from here https://www.python.org/downloads/)

	Then run cmd (win+r -> cmd) and type:
	>pip install selenium
        >pip install pyautogui
        >pip install opencv-python
        >pip install pycopy-audioop

        >pip install pipwin (only for installing pyadio)
        >pipwin install pyaudio

	Also don't forget to set the stereo mixer as default!

	After that run main.py in cmd:
		>python [DIR_WHEN_MAINPY_IS_LOCATED]\main.py

        OR 

        Right click on main.py -> Run Python File in Terminal

### ABOUT ###
    After you ran the main.py, the following will appear:
        Select option:    
            1 - go to
            2 - exit

    start option is used for navigating to the url, and then record contents
        options of start:
            - url of youtube video
            - filename in which contents will stored ( Create a new empty folder for storing )
            - duration of recording (in seconds)

    exit closes script