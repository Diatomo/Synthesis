

#TODO test incomplete file names
class Parser:

    def __init__(self):
       self.song = {}
       self.f = ''

    def printSong(self):
        for key, value in self.song.items():
            print(key)
            print(value)

    def loadFile(self, f):
        self.f = open(f,'r+')

    def parse(self):
        if (self.f != ''):
            sectionName = ''
            notes = []
            section = False
            for line in self.f:
                line = line[:-1]
                
                #section is reached
                if (len(line) > 1 and not section):
                    sectionName = line
                    section = True

                #gather notes in section
                elif (len(line) > 1 and section and line != 'END'):
                    temp = line.split(',') #temporary line of notes
                    for note in temp:
                        notes.append(note)

                #notes done appending
                elif (len(line) < 1 and section or line == 'END'):
                    section = False
                    self.song[sectionName] = notes
                    sectionName = ''
                    notes = []
        else:
            println("Incorrect format")


class Randomizer:

    def __init__(self):
        self.length = 32
        self.octaveMin = 2
        self.octaveMax = 6
        self.notes = ['A','B','C','D','E','F','G']
        self.octaves = range(self.octaveMin, self.octaveMax)
        self.song = {}
        self.notes = []


    def printNotes(self):
        print(self.notes)

    def printSong(self):
        for key, value, in self.song.items():
            print(key)
            print(value)

    def changeLength(self, length):
        self.length = length

    def setScale(self,scale):
        pass

    def pure(self):
        for note in range(self.length):
            note = self.notes[randrange(len(self.notes))]
            octave = self.octaves[randrange(len(self.octaves))]
            self.notes.append(note + str(octave))



