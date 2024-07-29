## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_clock.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from datetime import datetime, timezone
import matplotlib.pyplot as plt
import os
import numpy as np

# Initialization, define some constant
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = path + '/samples' + '/airplane.bmp'
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
gmt_hand_length = 120
gmt_hand_width = 4
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig, ax = plt.subplots()
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

while True:
    plt.imshow(background)
    plt.axis('off')
    
    # Retrieve the time
    now_time = datetime.now()
    utc_time = datetime.now(timezone.utc)
    
    hour = now_time.hour
    minute = now_time.minute
    second = now_time.second
    gmt_hour = utc_time.hour

    # Calculate angles for clock hands
    hour_angle = (hour % 12 + minute / 60 + second / 3600) * (2 * np.pi / 12)
    minute_angle = (minute + second / 60) * (2 * np.pi / 60)
    second_angle = second * (2 * np.pi / 60)
    gmt_angle = gmt_hour * (2 * np.pi / 24)

    # Calculate end points of hour, minute, second, and GMT hands
    hour_vector = clock_hand_vector(hour_angle, hour_hand_length)
    minute_vector = clock_hand_vector(minute_angle, minute_hand_length)
    second_vector = clock_hand_vector(second_angle, second_hand_length)
    gmt_vector = clock_hand_vector(gmt_angle, gmt_hand_length)

    # Draw clock hands
    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], 
              head_length=3, linewidth=hour_hand_width, color='black')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], 
              linewidth=minute_hand_width, color='black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], 
              linewidth=second_hand_width, color='red')
    plt.arrow(center[0], center[1], gmt_vector[0], gmt_vector[1], 
              linewidth=gmt_hand_width, color='yellow')

    plt.pause(0.1)
    plt.clf()