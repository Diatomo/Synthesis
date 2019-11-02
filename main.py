

from communication import DAC
from parser import Parser



baseNotes = ['A','B','C','D','E','F','G']
octaves = ['2','3','4','5','6']
notes = []

for octave in octaves:
    for note in baseNotes:
        notes.append(note+octave)

def main():
    '''
    fn = 'fairyFountain'
    par = Parser()
    par.loadFile(fn)
    par.parse()
    par.printSong()
    print("fin")
    '''
    k = 4
    n = len(notes)
    permute(notes,"", n, k)

def permute(notes, prefix, n, k):
    
    if (k == 0):
        print(prefix)
        return

    for i in range(n):
        newPrefix = prefix + notes[i]

        permute(notes, newPrefix, n, k-1)

main()
