#!/usr/bin/env python

import rospy
from beginner_tutorials.srv import detectobject, detectobjectResponse
import serial

def handle_detect_object(req):
    try:
        # Connect to the MaxBotix sensor via USB
        ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)  # Adjust port if necessary
        raw_data = ser.readline().decode('utf-8').strip()  # Read sensor data
        ser.close()

        # Convert data to float
        distance = float(raw_data)

        # Log distance and threshold
        rospy.loginfo(f"Distance: {distance} cm, Threshold: {req.threshold} cm")

        # Determine result based on threshold
        result = "ada objek" if distance <= req.threshold else "tidak ada objek"

        # Return result to client
        return detectobjectResponse(result)

    except Exception as e:
        rospy.logerr(f"Error reading sensor: {e}")
        return detectobjectResponse("Error")

def detect_object_server():
    rospy.init_node('detect_object_server')  # Initialize ROS node
    service = rospy.Service('detect_object', detectobject, handle_detect_object)
    rospy.loginfo("Detect Object Server is ready.")
    rospy.spin()

if __name__ == "__main__":
    detect_object_server()
