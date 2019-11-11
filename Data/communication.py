import os
import time
from random import randrange

''' test variables '''
#message = str(INSTR) + ' ' + str(3) + ';'



#TODO communication params
#TODO instrument
class DAC:

    def __init__(self):
        self.rootFreq = 440.0 #tuning
        self.beats = 140
        self.bpm = 1.0 / (beats / 60.0)

    def send2Pd(self, message=''):
        os.system("echo '" + str(message)  + "' | pdsend 3000")

    '''
        fxn : hasAccent
        @midi :: current midi note
        returns a boolean
        description :: checks if the note contains an accent
                       which determines ascend or descend

    '''
    def hasAccent(self, midi):
        accent = False
        for let in midi:
            if let == 'b' or let == '#':
                accent = True
        return accent

    '''
        fxn : getNotes
        @midi : current midi note
        description :: returns an array of possible midi notes
    '''
    def getNotes(self, midi):
        notes = ['C','C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        if (self.hasAccent(midi)):
            if (midi[1] == 'b'):
                notes = ['C', 'Db', 'D', 'Eb' 'E','F', 'Gb', 'G', 'Ab', 'A', 'Bb' 'B']
        return notes

    '''
        fxn : naturalize
        @midi :: current midi note to be naturalized
        description naturalizes an E or F
    '''
    def naturalize(self, midi):
        natural = midi
        if (natural[0] == 'E'):
            natural = 'F' + midi[-1]
        else:
            natural = 'E' + midi[-1]
        return natural

    '''
        fxn :: accent
        @rootNote :: root (A4)
        @midiNote :: current midi note
        @rootOctave :: octave of root note (4)
        @midiOctave :: current octave of midi note
        @notes :: list of possible notes
        description :: ascends converting midi notes to frequencies
    '''
    def ascent(self, rootNote, midiNote, rootOctave, midiOctave, notes):
        distance = 0
        #iteration
        while (rootNote != midiNote or int(rootOctave) != int(midiOctave)):
            temp = notes.index(rootNote)
            rootNote = notes[(temp + 1) % len(notes)]
            if ((temp+1) % len(notes) == 0):
                rootOctave += 1
            distance += 1
        return distance

    '''
        fxn :: descent
        @rootNote :: root (A4)
        @midiNote :: current midi note
        @rootOctave :: octave of root note (4)
        @midiOctave :: current octave of midi note
        @notes :: list of possible notes
        description :: descends converting midi notes to frequencies
    '''
    def descent(self, rootNote, midiNote, rootOctave, midiOctave, notes):
        distance = 0
        #iteration
        while (rootNote != midiNote or int(rootOctave) != int(midiOctave)):
            temp = notes.index(rootNote)
            rootNote = notes[(temp - 1) % len(notes)]
            if ((temp+1) % len(notes) == 0):
                rootOctave -= 1
            distance -= 1
        return distance


    def dist(self, midi):

        #alias
        rootNote = 'A'
        rootOctave = 4
        midiOctave = midi[-1]
        notes = self.getNotes(midi)
        distance = 0
        descend = True
        accent = False
        
        #exception check
        if ((midi[0] == 'E' or midi[0] == 'F') and self.hasAccent(midi)):
            midi = self.naturalize(midi)
     
        #set equiv for while loop
        if (self.hasAccent(midi)):
            midiNote = midi[0:2]
        else:
            midiNote = midi[0]

        #main iteration
        noteComp = notes.index(midi[0]) > notes.index('A')
        octComp = int(midi[-1] > int(rootOctave))
        if (int(midi[-1]) > int(rootOctave)):
            distance = self.ascent(rootNote, midiNote, rootOctave, midiOctave, notes)
        elif (int(midi[-1]) < int(rootOctave)):
            distance = self.descent(rootNote, midiNote, rootOctave, midiOctave, notes)
        else:
            if (noteComp):
                distance = self.ascent(rootNote, midiNote, rootOctave, midiOctave, notes)
            elif (not noteComp):
                if (notes.index(midi[0]) == notes.index('A')):
                    if (hasAccent):
                        distance = 1
                else:
                    distance = self.descent(rootNote, midiNote, rootOctave, midiOctave, notes)
        return distance

    ''' turn midi data into frequency data for purr data '''
    def noteToFreq(self, note):
        a = (2.0)**(1/12.0)
        freq = rootFreq * (a**self.dist(note))
        return freq

    ''' communication functions '''
    def turnOn(self, note):
        message = str(SWITCH) + ' ' + str(ON) + ';'
        send2Pd(message)
        message = str(NOTE) + ' ' + str(note) + ';'
        send2Pd(message)

    def turnOff(self, note):
        message = str(SWITCH) + ' ' + str(0) + ';'
        send2Pd(message)
        message = str(NOTE) + ' ' + str(note) + ';'
        send2Pd(message)

    '''
        fxn :: play
        description :: plays midi notes
        and converts them to frequencies
    '''
    def play(self, freq):
        for midi in freq:
            note = self.noteToFreq(midi)
            turnOn(note)
            time.sleep(self.bpm)
            turnOff(note)
