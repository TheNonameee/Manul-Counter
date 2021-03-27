import pyttsx3

import time

manulcounter = 1
timersleep = 1


def manulsound(manul):
    engine = pyttsx3.init()

    if(manul % 10 == 1):
        if(manul % 100 == 11):
            engine.say(str(manul) + "manulov")

            engine.runAndWait()

        else:
            engine.say(str(manul) + "manul")

            engine.runAndWait()

    elif(manul % 10 == 2):
        if(manul % 100 == 12):
            engine.say(str(manul) + "manulov")

            engine.runAndWait()

        else:
            engine.say(str(manul) + "manula")

            engine.runAndWait()

    elif(manul % 10 == 3):
        if(manul % 100 == 13):
            engine.say(str(manul) + "manulov")

            engine.runAndWait()

        else:
            engine.say(str(manul) + "manula")

            engine.runAndWait()

    elif(manul % 10 == 4):
        if(manul % 100 == 14):
            engine.say(str(manul) + "manulov")

            engine.runAndWait()

        else:
            engine.say(str(manul) + "manula")

            engine.runAndWait()

    elif(manul % 10 == 5):
        engine.say(str(manul) + "manulov")

        engine.runAndWait()

    elif(manul % 10 == 6):
        engine.say(str(manul) + "manulov")

        engine.runAndWait()

    elif(manul % 10 == 7):
        engine.say(str(manul) + "manulov")

        engine.runAndWait()

    elif(manul % 10 == 8):
        engine.say(str(manul) + "manulov")

        engine.runAndWait()

    elif(manul % 10 == 9):
        engine.say(str(manul) + "manulov")

        engine.runAndWait()

    elif(manul % 10 == 0):
        engine.say(str(manul) + "manulov")

        engine.runAndWait()


while True:
    manulsound(manulcounter)
    manulcounter = manulcounter + 1

    time.sleep(timersleep)