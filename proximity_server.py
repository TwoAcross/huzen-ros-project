#!/usr/bin/env python

from beginner_tutorials.srv import ProximitySensor, ProximitySensorResponse
import rospy
import serial

def handle_proximity_sensor(req):
    # Example logic: let's assume you already read sensor data here.
    # Replace `sensor_data` with your actual sensor reading.
    sensor_data = 50  # Replace this with actual sensor logic.

    # Logic to determine if an object is detected
    object_detected = sensor_data < 100  # Adjust threshold as necessary.

    print("Proximity sensor data:", sensor_data)
    print("Object detected:", object_detected)

    return ProxBooleanResponse(object_detected)

def proximity_sensor_server():
    rospy.init_node('proximity_server')
    s = rospy.Service('proximity_sensor', ProxBoolean, handle_proximity_sensor)
    print("Proximity sensor service is ready.")
    rospy.spin()

if __name__ == "__main__":
    proximity_server()
