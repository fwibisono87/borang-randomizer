import random
import time
listnama = ["Afnadiati   ", "Francis     ", "Naufal PY   ", "Priyanti N  ", "Radhiansya  ", "Raihan R M  ", "Timothy EH  "]
print ("Nilai Borang B1 Generator")
print ("Made for HG3 MPKTB kelas H")
input("Press enter to continue... ")
print ("")
repeater = 0
while (repeater<1):
    for nama in listnama:
        x = str(nama)
        a=random.randint(4,5)
        b=random.randint(4,5)
        c=random.randint(4,5)
        d=random.randint(4,5)

        print (x, a, b, c, d)
        print (" ")
    adder = input("Press enter to repeat randomization. Press 1 to exit. ")
    if adder.isdigit():
        adder = int(adder)
        repeater = repeater+adder
    
print ("Terminating Program...")
time.sleep(1)
quit()
