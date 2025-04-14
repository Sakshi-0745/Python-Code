import time
try:
    sec = int(input("enter the time in seconds : "))
    while sec:
        mins, sec = divmod(sec, 60)
        timer = f'{mins:02d}:{sec:02d}'
        print(f"Time Left : {timer}", end = '\r')
        time.sleep(1)
        sec -= 1
    print("Time's up!")
except ValueError:
    print("Please enter a valid number of seconds.")