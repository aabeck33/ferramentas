import winsound

for freq in range(40, 20000, 80):
    winsound.Beep(freq, 600)
    print(freq)
