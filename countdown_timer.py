import time

hours, minutes, seconds = input("Enter the time in the format (HH MM SS): ").split() # this splits the string input into a list that contains the values and each value in the list is assigned based on the variables on the lhs
hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)

time_up = False
while not time_up:
    print("{:02d}:{:02d}:{:02d}".format(hours,minutes,seconds))
    seconds -= 1
    if seconds == 0 and minutes != 0:
        minutes -= 1
        seconds = 60
    if minutes == 0 and hours != 0:
        seconds = 60
        hours -= 1
        minutes = 60
        minutes -= 1
    time.sleep(1)
    if hours == 0 and seconds == 0 and minutes == 0:
        print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
        time_up = True
        print("Time up!")













