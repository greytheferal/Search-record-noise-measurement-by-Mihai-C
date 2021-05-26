import video_record
import audio_record

from config import *
from os import mkdir
from os.path import exists
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class DriverHandler():
    
    def __init__(self):
        self.driver = self.create_new_driver()
        self.navigate()

    def start_recordings(self, filename : str, duration : int = 7) -> None:
        if not exists(PATH+filename):
            mkdir(PATH+filename)
        a_recorder = audio_record.AudioRecordHandler(filename+'\\'+filename)
        v_recorder = video_record.VideoRecordHandler(filename+'\\'+filename)
        a_recorder.start_recording(duration)
        v_recorder.start_recording(duration)
        a_recorder.thread.join()
        v_recorder.thread.join()
        a_recorder.discard()
        v_recorder.discard()

    def navigate(self, site : str = 'https://www.youtube.com/') -> None:
        if self.driver != None:
            try:
                self.driver.get(site)
                if site != 'https://www.youtube.com/':
                    self.maximize_video()
            except:
                pass
            
    def play_video(self) -> None:
        #clicking on play button 
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[@class="ytp-play-button ytp-button"]'))).click()
        except:
            pass

    def maximize_video(self) -> None:
        #clicking on maximize button 
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[@class="ytp-fullscreen-button ytp-button"]'))).click() 
        except:
            pass

    def create_new_driver(self) -> Chrome:
        return Chrome(executable_path=PATH+'chromedriver.exe', options=self.create_new_options())
    
    def create_new_options(self) -> ChromeOptions:
        options = ChromeOptions()

        # remove pop-up with: 'browser is controlled by...'
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        # also removes other pop-ups
        options.add_argument('--disable-notifications')

        # set window size
        options.add_argument('--start-maximized')

        return options

if __name__ == '__main__':
    print('Try main.py...')