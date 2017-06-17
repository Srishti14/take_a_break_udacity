import time
import webbrowser

total_breaks = 3
count_breaks = 0

while(count_breaks < total_breaks):
    time.sleep(30*60)
    webbrowser.open("https://youtu.be/VuNIsY6JdUw")
    count_breaks = count_breaks + 1
