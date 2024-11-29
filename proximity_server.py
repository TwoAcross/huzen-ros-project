#!/usr/bin/env python

from __future__ import print_function
from beginner_tutorials.srv import ProxBoolean, ProxBooleanResponse
import rospy
import serial  # For serial communication
import re      # For parsing the "Rxxxx" format

def handle_proximity_request(req):
    try:
        # Adjust the serial port and baud rate to match your setup
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.flush()

        if ser.in_waiting > 0:
            # Read the raw data and decode it
            line = ser.readline().decode('utf-8').strip()
            print(f"Raw data received: {line}")

            # Match the "Rxxxx" format using a regular expression
            match = re.match(r"R(\d+)", line)
            if match:
                distance = int(match.group(1))  # Extract the numeric part
                print(f"Parsed distance: {distance} cm")

                # Check if an object is detected (threshold: 30 cm)
                detected = distance < 30
                return ProxBooleanResponse(detected)
            else:
                print("Error: Invalid data format received")
                return ProxBooleanResponse(False)  # Assume no object detected on error
    except Exception as e:
        print(f"Error reading from sensor: {e}")
        return ProxBooleanResponse(False)  # Assume no object detected on error

def proximity_server():
    rospy.init_node('proximity_server')
    service = rospy.Service('proximity_sensor', ProxBoolean, handle_proximity_request)
    print("Proximity Sensor Server is ready.")
    rospy.spin()

if __name__ == "__main__":
    proximity_server()
