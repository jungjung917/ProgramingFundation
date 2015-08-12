import webbrowser
import time

n_Break = 3
n_count = 1

print ("This program started on:"+ time.ctime())
#print ("Let's go to watch the movie!")
while (n_count<= n_Break):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=10r9ozshGVE", new=0, autoraise=True)
    n_count+=1
