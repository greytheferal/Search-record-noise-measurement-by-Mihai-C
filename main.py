from typing import Counter
from driver import DriverHandler

def goto(driver : DriverHandler) -> None:
    url = None
    filename = None
    duration = None
    while True:
        print('Enter: url, filename, duration:')
        try:
            url =          input('    url: ')
            filename =     input('    filename: ')
            duration = int(input('    duration: '))

            print('Navigating...')
            driver.navigate(url)
            # trying to skip possible ad
            driver.navigate(url)
            driver.start_recordings(filename, duration)
            driver.play_video()
            return
        except:
            if input('Something went wrong! Do you wanna exit (y/n)? :').lower() == 'y':
                return

def interact() -> None:
    print('Starting...')
    driver = DriverHandler()
    while True:
        try:
            choise = int(input('Select option:\n    1 - go to\n    2 - exit\n'))
            if choise not in range(1,3):
                print('Your choise must be 1 or 2!')
            else:
                if choise == 1:
                    goto(driver)
                elif choise == 2:
                    break
                else:
                    continue
        except:
            if input('Something went wrong! Do you wanna exit (y/n)? :').lower() == 'y':
                break

if __name__ == '__main__':
    interact()