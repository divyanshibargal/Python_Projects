import pyttsx3
if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome I am your Robo Speaker")
    while True:
        x = input("Enter what you want me to speak : ")
        if x == 'q':
            engine.say("Bye Bye Friends")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()