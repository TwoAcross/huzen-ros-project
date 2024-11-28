#!/usr/bin/env python

from __future__ import print_function
from beginner_tutorials.srv import ProxBoolean, ProxBooleanResponse
import rospy
import serial  # Untuk komunikasi serial

def handle_proximity_request(req):
    try:
        # Ganti '/dev/ttyUSB0' dengan port serial sensor
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.flush()

        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            distance = float(line)  # Asumsi sensor mengirimkan jarak dalam format float
            print(f"Distance received: {distance} cm")
            
            # Jika jarak kurang dari treshold (30) , objek terdeteksi
            detected = distance < 30.0
            return ProximitySensorResponse(detected)
    except Exception as e:
        print(f"Error reading from sensor: {e}")
        return ProximitySensorResponse(False)  # Jika error, anggap objek tidak terdeteksi

def proximity_server():
    rospy.init_node('proximity_server')
    service = rospy.Service('proximity_sensor', ProxBoolean, handle_proximity_request)
    print("Proximity Sensor Server is ready.")
    rospy.spin()

if __name__ == "__main__":
    proximity_server()
