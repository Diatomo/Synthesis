


import os
import time
from random import randrange

def send2Pd(message=''):
    os.system("echo '" + str(message)  + "' | pdsend 3000")

SWITCH = 0
NOTE = 1
INSTR = 2

ON = 1
OFF = 0
note = 500
instr = 2



''' calculation frequency information '''
def hasAccent(midi):
    accent = False
    for let in midi:
        if let == 'b' or let == '#':
            accent = True
    return accent

def getNotes(midi):
    notes = ['C','C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    if (hasAccent(midi)):
        if (midi[1] == 'b'):
            notes = ['C', 'Db', 'D', 'Eb' 'E','F', 'Gb', 'G', 'Ab', 'A', 'Bb' 'B']
    return notes

def naturalize(midi):
    natural = midi
    if (natural[0] == 'E'):
        natural = 'F' + midi[-1]
    else:
        natural = 'E' + midi[-1]
    return natural

def ascent(rootNote, midiNote, rootOctave, midiOctave, notes):
    distance = 0
    #iteration
    while (rootNote != midiNote or int(rootOctave) != int(midiOctave)):
        temp = notes.index(rootNote)
        rootNote = notes[(temp + 1) % len(notes)]
        if ((temp+1) % len(notes) == 0):
            rootOctave += 1
        distance += 1
    return distance

def descent(rootNote, midiNote, rootOctave, midiOctave, notes):
    distance = 0
    #iteration
    while (rootNote != midiNote or int(rootOctave) != int(midiOctave)):
        temp = notes.index(rootNote)
        rootNote = notes[(temp - 1) % len(notes)]
        if ((temp+1) % len(notes) == 0):
            rootOctave -= 1
        distance -= 1
    return distance


def dist(midi):

    #alias
    rootNote = 'A'
    rootOctave = 4
    midiOctave = midi[-1]
    notes = getNotes(midi)
    distance = 0
    descend = True
    accent = False
    
    #exception check
    if ((midi[0] == 'E' or midi[0] == 'F') and hasAccent(midi)):
        midi = naturalize(midi)
 
    #set equiv for while loop
    if (hasAccent(midi)):
        midiNote = midi[0:2]
    else:
        midiNote = midi[0]

    #main iteration
    noteComp = notes.index(midi[0]) > notes.index('A')
    octComp = int(midi[-1] > int(rootOctave))
    if (int(midi[-1]) > int(rootOctave)):
        distance = ascent(rootNote, midiNote, rootOctave, midiOctave, notes)
    elif (int(midi[-1]) < int(rootOctave)):
        distance = descent(rootNote, midiNote, rootOctave, midiOctave, notes)
    else:
        if (noteComp):
            distance = ascent(rootNote, midiNote, rootOctave, midiOctave, notes)
        elif (not noteComp):
            if (notes.index(midi[0]) == notes.index('A')):
                if (hasAccent):
                    distance = 1
            else:
                distance = descent(rootNote, midiNote, rootOctave, midiOctave, notes)
    return distance

''' test variables '''
message = str(INSTR) + ' ' + str(3) + ';'
send2Pd(message)
beats = 140
BPM = 1.0 / (beats / 60.0)


''' turn midi data into frequency data for purr data '''
def noteToFreq(note):
    rootFreq = 440.0 #tuning
    a = (2.0)**(1/12.0)
    freq = rootFreq * (a**dist(note))
    return freq

''' communication functions '''
def turnOn(note):
    message = str(SWITCH) + ' ' + str(ON) + ';'
    send2Pd(message)
    message = str(NOTE) + ' ' + str(note) + ';'
    send2Pd(message)

def turnOff(note):
    message = str(SWITCH) + ' ' + str(0) + ';'
    send2Pd(message)
    message = str(NOTE) + ' ' + str(note) + ';'
    send2Pd(message)

'''
freq = ['A3', 'G3', 'F#3', 'G3', 'G3', 'F3', 'E3', 'F3', 'F3', 'E3', 'D#3', 'E3', 'D3', 'C#3', 'D3'
        'A3', 'G3', 'F#3', 'G3', 'C#3', 'A3', 'G#3', 'A3', 'C4', 'C#3', 'A3', 'C#3', 'A3', 'G3', 'F3', 'E3']
#for inst in range(4):
 #   message = str(INSTR) + ' ' + str(inst) + ';'
  #  send2Pd(message)
for midi in freq:
    note = noteToFreq(midi)
    turnOn(note)
    time.sleep(BPM)
    turnOff(note)


freq = ['D1', 'C2', 'C2', 'E2', 'C1', 'A1', 'C1', 'E2', 'B0', 'A1', 'B0', 'B1', 'A0', 'G1', 'A0', 'B1'
'D1', 'C2', 'D1', 'F1', 'C1', 'E1', 'F1', 'F#1', 'B0', 'B0', 'E1', 'E1', 'E1', 'D1', 'E1', 'G1']
for midi in freq:
    note = noteToFreq(midi)
    turnOn(note)
    time.sleep(BPM)
    turnOff(note)
'''

def play(freq):
    for midi in freq:
        note = noteToFreq(midi)
        turnOn(note)
        time.sleep(1.0 / (randrange(70,160) / 60.0))
        turnOff(note)
'''
tempNotes = ['C','C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
def testChart():
    for octave in range(9):
        for note in tempNotes:
            print((note + str(octave)) + ' ' + str(noteToFreq(note+str(octave))))

testChart()
'''


#TODO list comprehension
def randomizer():
    length = 32
    freqs = []
    notes = ['A','B','C','D','E','F','G']
    octaves = [0,1,2,3,4,5,6,7,8]
    for note in range(length):
        note = notes[randrange(len(notes))]
        octave = octaves[randrange(2,len(octaves)-3)]
        freqs.append(note + str(octave))
    print(freqs)
    return freqs

for plays in range(5):
    play(randomizer())

    



















































