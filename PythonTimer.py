import time

print("Insturction: Enter time")
my_time = int(input("Set Timer:"))
print("TIMER START")

for x in range(1, my_time):
    print(x)
    time.sleep(1)
print("Time Out")