import webbrowser
import time

index = 0
print ("This program started on " + time.ctime())
while index < 3:
    time.sleep(10)
    webbrowser.open("youtube.com")
    index = index + 1
