import math
import audioop

# https://stackoverflow.com/questions/25868428/pyaudio-how-to-check-volume
def decibels(data) -> int:
    return int(20 * math.log10(audioop.rms(data, 2)))

if __name__ == '__main__':
    print('Try main.py...')