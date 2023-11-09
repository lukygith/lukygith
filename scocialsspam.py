#ngllinkspammer
import time
import keyboard

a =input("Jakou zpravu si prejete napsat: ")
b = input("Kolikrat si prejete zpravu odeslat: ")
print(a)
print(b)

print("Otevrete ngl link")

time.sleep(5)

for i in range(int(b)):

    keyboard.write(a)
    keyboard.write("a")
    time.sleep(1)
    keyboard.press_and_release("tab")
    time.sleep(1)
    keyboard.press_and_release("enter")

    keyboard.press_and_release("tab")
    time.sleep(0.2)
    keyboard.press_and_release("tab")
    time.sleep(0.2)
    keyboard.press_and_release("tab")
    time.sleep(0.2)
    keyboard.press_and_release("enter")
    time.sleep(1)
    keyboard.press_and_release("tab")
    time.sleep(0.2)

    print("Konec")