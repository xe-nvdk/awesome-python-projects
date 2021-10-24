# line protocol data generator by Ignacio Van Droogenbroeck

import random
import time

measurement = ["cpu_load_short", "memory"]
tag_key = ["host"]
tag = ["server01", "server02"]
fields = ["load", "used"]
values = random.sample(range(1, 100), 30)
timestamp = int(time.time())

writer = open("data.txt", "w")

while True:
    for i in range(len(values)):
        line = "{0},{1}={2} {3}={4} {5}\n".format(measurement[0], tag_key[0], tag[0], fields[0], values[i], timestamp)
        writer.write(line)
        timestamp += 10
        time.sleep(0.1)