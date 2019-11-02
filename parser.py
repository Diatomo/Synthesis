


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



