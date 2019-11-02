

from communication import DAC
from parser import Parser

def main():
    fn = 'fairyFountain'
    par = Parser()
    par.loadFile(fn)
    par.parse()
    par.printSong()
    print("fin")


main()
