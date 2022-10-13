#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import adafruit_bno055
import board
from datetime import datetime
import time
import csv

i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

now = datetime.now()
creation = now.strftime("%d-%m-%Y-%H-%M-%S")

header = ['time','x','y','z','total']

with open('{}.csv'.format(creation), 'w') as f:
    # create the csv writer
    writer = csv.writer(f)
    writer.writerow(header)

    start_time = time.time()
    time = time.time() - start_time
    while time < 180:
        time = time.time() - start_time
        x, y, z = sensor.acceleration
        total = abs(x) + abs(y) + abs(z)
        row = [time, x, y, z, total]
        writer.writerow(header)

