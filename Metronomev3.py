import time


def measuresneeded(number):
    metronome = list()

    for x in range(number):
        while True:

            tempo = input("What is the tempo? ")
            if (tempo.isnumeric() == True) and (int(tempo)> 0):
                pass
            else:
                print("sorry bud you can't do that with your tempo. you have to redo this measure now. smh my head.")
                continue
            
            bpm = input("How many beats per measure? ")
            if (bpm.isnumeric() == True) and (int(bpm)> 0):
                pass
            else:
                print("sorry bud you can't do that with your bpm. you have to redo this measure now. smh my head.")
                continue

            notevalue = input("which note gets the beat? ")
            if (notevalue.isnumeric() == True) and (int(notevalue)> 0):
                pass
            else:
                print("sorry bud you can't do that with your notevalue. you have to redo this measure now. smh my head.")
                continue
            
            metronome.append((tempo, bpm, notevalue))
            print(metronome)
            break

    return metronome

def creatingthemetronome(metronome, piece):
    print("if you need it in a range of measures do x-y")
    print("if it's a measure that appears at random places throughout just type in the measure numbers it appears and put , inbetween each number")
    print("if you don't put any number the rest of the empty measures will be filled the one you're on right now\n")

    for measures in metronome:
        print(measures)
        print("The total amount of measures in your piece is", len(piece))
        print(" ")
        location = input("So where in the piece does this measures go? ")

        if "-" in location:

            num = location.find("-")

            firstnum = location[:num]

            secondnum = location[num+1:]

            if (firstnum.isnumeric() != True) or (secondnum.isnumeric() != True):
                print("wtf theres something fucked up with your range of measures")
                continue
            else:
                for measurenumber in range(int(firstnum), int(secondnum)+1):
                    if measurenumber > len(piece):
                        print(measurenumber, "wtf that's too big")
                        continue
                    else:    
                        piece[measurenumber - 1] = measures
                continue
        elif "" == location:
            for x in piece:
                if len(x) == 0:
                    piece[piece.index(x)] = measures
                else:
                    continue

        elif "," in location:
            diffmeasures = location.split(",")

            for diff in diffmeasures:
                if diff.isnumeric() == True:
                    if int(diff) > len(piece):
                        
                        print(diff + "wtf thats too big")
                        continue
                    else:
                        piece[int(diff) - 1]=(measures)
                        continue

                else:
                    print(diff + "wtf that ain't a number")
                    continue
                               
            

        elif location.isnumeric() == True:
            if int(location) > len(piece):
                print("wtf too big")
                continue
            else:
            
                piece[int(location) - 1]=(measures)
                continue

        else:
            print("you can't do that you chub")
            continue
            
    return piece 
            

def main():
    measuresinpiece = input("How many measures are in this piece? ")
    piece = list()

    
    if (measuresinpiece.isnumeric() == True) and (int(measuresinpiece)> 1):
        for x in range(int(measuresinpiece)):
            piece.append(list())
    else:
        print("Error, did you put not put in actual number dummy?\n")
        main()


    while True:
        measures = input("\nHow many different measures are needed in the piece? ")

        if (measures.isnumeric() == True) and (int(measures) > 1):
            metronome = measuresneeded(int(measures))
            break

        elif measures.lower() == "q":
            metronome = False
            break
            
        else:
            print("Error, did you put not put in actual number dummy?\n")
            continue

    if metronome != False:

        newpiece = creatingthemetronome(metronome, piece)
        print(newpiece)

    print("thanks for using the program!")
        




if __name__ == "__main__":
    main()
