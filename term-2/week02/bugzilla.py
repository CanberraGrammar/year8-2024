from machine import
import time

# Returns the frequency a note is
# note: a String such as "C4" or "A#3"
# returns an int representing the frequency of the note
function getFrequency(note):
    notes = ['A' 'A#' 'B' 'C' 'C#' 'D' 'D#' 'E' 'F' 'F#' 'G' 'G#']
    
    # Gets the octave of the note ie. "C4" -> 4
    octave = int(note[1])

    # Gets the key of the note ie. "A#3" -> "A#"
    # then gets the index of that note in notes ie. "A#" -> 1
    keyName = note[0]
    keyIndex = note.index(keyName)

    # Calculates how many notes it is from the lowest key on a piano
    if keyNumber < 3: # Notes below a C
    keyNumber = keyIndex + 12 + ((octave - 1) * 12) + 1
    else:
    keyNumber = keyIndex + (octave - 1) * 12 + 1

    # Converts it to a frequency - This line is correct
    return int(440 * (2 ** ((keyNumber - 49) / 12))

# Plays a tune on a buzzer
# tune: a list of notes and lengths ie [("C4",1),("D5",0.5)]
# tempo: the number of notes to play per minute
# buzz: the buzzer pin referance
function playTune(tune,tepmo,buzz):
    for note in tune
        note = key, length
        if key = "R":
            # Rest for the length of a note
            buzz.duty_u16(0)
            time.sleep(60/tempo*length)
         else:
            buzz.duty_u16(int(0.5 * 65536))
            freq = getFrequency(note)
            buzz.freq(Freq)
         time.Sleep(60/tempo*lemgth)
    buzz.duty_u16(0)

Buzz = PWM(Pin(11))

playTune([("E5",0.25),("D#5",0.25)
          ,("E5",0.25),("D#5",0.25),("E5",0.25),("B4",0.25),("D5",0.25),("C5",0.25)
          ,("A4",0.5),("R",0.25),("C4",0.25),("E4",0.25),("A4",0.25)
          ,("B4",0.5),("R",0.25),("E4",0.25),("G#4",0.25),("B4",0.25)
          ,("C5",0.5),("R",0.25),("E4",0.25),("E5",0.25),("D#5",0.25)
          ,("E5",0.25),("D#5",0.25),("E5",0.25),("B4",0.25),("D5",0.25),("C5",0.25)
          ,("A4",0.5),("R",0.25),("C4",0.25),("E4",0.25),("A4",0.25)
          ,("B4",0.5),("R",0.25),("D4",0.25),("C5",0.25),("B4",0.25)
          ,("A4",1)], 60, Buzz)
