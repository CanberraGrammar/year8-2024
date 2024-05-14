from machine import *
import time

def getFrequency(note):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    
    if len(note) == 3:
        octave = int(note[2])
    else:
        octave = int(note[1])

    keyNumber = int(notes.index(note[:-1]))

    if keyNumber < 3: # Notes below a C
        keyNumber = keyNumber + 12 + ((octave - 1) * 12) + 1
    else:
        keyNumber = keyNumber + (octave - 1) * 12 + 1

    return int(440 * (2 ** ((keyNumber - 49) / 12)))

def playTune(tune,tempo,buzz):
    for note in tune:
        key, length = note
        if key == "R":
            buzz.duty_u16(0)
        else:
            buzz.duty_u16(int(0.5 * 65536))
            freq = getFrequency(key)
            buzz.freq(freq)
        time.sleep(60/tempo*length)
    buzz.duty_u16(0)

Buzz = PWM(Pin(16))

playTune([("E5",0.25),("D#5",0.25)
          ,("E5",0.25),("D#5",0.25),("E5",0.25),("B4",0.25),("D5",0.25),("C5",0.25)
          ,("A4",0.5),("R",0.25),("C4",0.25),("E4",0.25),("A4",0.25)
          ,("B4",0.5),("R",0.25),("E4",0.25),("G#4",0.25),("B4",0.25)
          ,("C5",0.5),("R",0.25),("E4",0.25),("E5",0.25),("D#5",0.25)
          ,("E5",0.25),("D#5",0.25),("E5",0.25),("B4",0.25),("D5",0.25),("C5",0.25)
          ,("A4",0.5),("R",0.25),("C4",0.25),("E4",0.25),("A4",0.25)
          ,("B4",0.5),("R",0.25),("D4",0.25),("C5",0.25),("B4",0.25)
          ,("A4",1)
          ],60,Buzz)