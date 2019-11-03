

'''
    Class: Parser
    Description:
        This takes a file and parses it into different sections

'''
class Sequence(object):

    def __init__(self):
        self.song = {}
        self.notes = ['C','C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def printSong(self):
        for key, value, in self.song.items():
            print(key)
            print(value)

#TODO test incomplete file names
class Parser(Sequence):

    def __init__(self):
        super(Sequence, self).__init__()
        self.f = ''

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


'''
    Class: Randomizer
    Description:
        Produces random sequences from permutation
        or just randomly producing a string of notes
'''
class Randomizer(Sequence):

    def __init__(self):
        super(Sequence, self).__init__()
        self.length = 32
        self.octaveMin = 2
        self.octaveMax = 6
        self.octaves = range(self.octaveMin, self.octaveMax)
        self.allBars = []
        self.notes = ['C','C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def printNotes(self):
        print(self.notes)

    def printAllBars(self):
        print(self.allBars)

    def changeLength(self, length):
        self.length = length

    def setScale(self,scale):
        pass

    def random(self, length):
        tempSection = []
        if (len(self.allBars) == 0):
            for (bar in range(length)):
                tempSection.append(self.allBars(randrange(0,len(allBars))))
        return tempSection

    def pure(self):
        for note in range(self.length):
            note = self.notes[randrange(len(self.notes))]
            octave = self.octaves[randrange(len(self.octaves))]
            self.notes.append(note + str(octave))

    def permute(self, prefix, k):
        n = len(self.notes)
        #base case    
        if (k == 0):
            self.allBars.append(prefix)
            return

        #creates tree
        for i in range(n):
            newPrefix = prefix + self.notes[i]
            self.permute(newPrefix, k-1)


