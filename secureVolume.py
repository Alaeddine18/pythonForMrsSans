pSeuil = 2.3
vSeuil = 7.41
p = float(input("Please enter a pressure: "))
v = float(input("Please enter a volume: "))
if p > pSeuil and v > vSeuil:
    exit()
elif p > pSeuil:
    print("Please increase the volume !")
elif v > vSeuil:
    print("Please decrease the volume ! ")
else:
    print("Everything is good")

