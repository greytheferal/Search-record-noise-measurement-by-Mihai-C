import cv2
import pyautogui
import threading
import numpy as np

import time
from datetime import datetime

class VideoRecordHandler():

    def __init__(self, name : str, framerate : float = 20.0):
        self.name = name
        self.framerate = framerate 
        self.size = pyautogui.size()

        # using .mp4 codec because .avi saves with some quality problems
        self.codec = cv2.VideoWriter_fourcc(*'mp4v')
        self.record = cv2.VideoWriter(f"{self.name}.mp4", self.codec, self.framerate, (self.size))

    def start_recording(self, duration : int) -> None:             
        self.duration = duration
        self.thread = threading.Thread(target=self.record_frames)
        self.thread_is_running = True
        self.thread.start()

    def record_frames(self) -> None:
        prev = 0
        start = datetime.now()
        for i in range(int((self.duration+1) * self.framerate)):
            self.record_frame() 
        '''while ((datetime.now() - start).total_seconds() < self.duration) and (self.thread_is_running):
            time_elapsed = time.time() - prev
            # trying to normileze iterations to current fps
            if time_elapsed > (1/self.framerate)*2:
                prev = time.time()
                self.record_frame()'''
        
    def record_frame(self) -> None:
        frame = np.array(pyautogui.screenshot())
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.record.write(frame)

    def discard(self) -> None:
        if self.thread.is_alive():
            self.thread_is_running = False
        self.record.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    print('Try main.py...')