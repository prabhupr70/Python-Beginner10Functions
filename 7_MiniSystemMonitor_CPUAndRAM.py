#Mini System Monitor (CPU + RAM)
#https://www.facebook.com/pythonclcoding/posts/pfbid021Sa96kTScajbNpBRnGxLmGsN2aJmixE9QsRJ1rmPD8HxQTocFcS5VHG5NczJ7qSfl

import psutil, time, os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
    print("CPU Usage: " , psutil.cpu_percent(interval=1), "%")
    print("RAM Usage: " , psutil.virtual_memory().percent, "%")
    time.sleep(1)
