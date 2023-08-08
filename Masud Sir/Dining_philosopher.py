import threading
import random
import time

philosopher = 5
Chopstick = [False, False, False, False, False]  # একদম প্রথমে কেউ চপস্টিক হাতে নেয় নাই


def wait(n):  # চপস্টিক হাতে নিবে
    global Chopstick
    while Chopstick[n] == True:  # n তম চপস্টিক অলরেডি আরেকজন নিয়া নিছে, তাই ও অপেক্ষা করবে
        print("Waiting for chopstick ", n)

    Chopstick[n] = True


def signal(n):  # চপস্টিক রেখে দিবে
    global Chopstick
    Chopstick[n] = False


def eating(x, n):
    wait(n)  # তার বাম পাশের চপস্টিকের খালি থাকলে নিবে নইলে অপেক্ষা করবে
    wait((n + 1) % 5)  # তার ডান পাশের চপস্টিকের খালি থাকলে নিবে নইলে অপেক্ষা করবে

    print("Eating ", n)
    time.sleep(0.01)

    signal(n)  # বাম হাতের চপস্টিক রেখে দিবে
    signal((n + 1) % 5)  # ডান হাতের চপস্টিক রেখে দিল

    print("Thinking ", n)
    print(threading.current_thread().name)


for i in range(4):
    n = random.randint(0, 4)
    t = threading.Thread(target=eating, args=('x', n))
    t.start()
