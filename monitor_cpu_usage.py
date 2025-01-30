import psutil
import time

threshold = 80

def monitor_cpu_usage():

    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > threshold:
            print(f"CPU usage is high {cpu_usage}%")
        else:
            print(f"CPU usage is normal {cpu_usage}%")

        time.sleep(5)

if __name__ == "__main__":
    monitor_cpu_usage()