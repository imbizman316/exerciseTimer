import pyttsx3
import time
import random

choices = ["쌩쌩이", "꺽기", "빠르게넘기", "한발씩 뛰기"]

def playSound(sound):
    engine = pyttsx3.init()
    engine.say(f'이제 {sound} 하세요.')
    engine.runAndWait()

howlong = int(input("How long do you want to exercise?"))
extraExercise = input("Is there other exercise you want to add?")

if extraExercise != "":
    choices.append(extraExercise)

starttime = time.time()

while True:
    nowtime = time.time()
    resulttime = nowtime - starttime
    print(resulttime)
    if resulttime > howlong:
        playSound("그만")
        break
    time.sleep(5)
    say = random.choice(choices)
    playSound(say)

