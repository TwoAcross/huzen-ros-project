#!/usr/bin/env python

from __future__ import print_function
import rospy
from beginner_tutorials.srv import ProxBoolean

def proximity_client():
    rospy.wait_for_service('proximity_sensor')
    try:
        proximity_sensor = rospy.ServiceProxy('proximity_sensor', ProxBoolean)
        response = proximity_sensor()
        return response.detected
    except rospy.ServiceException as e:
        print(f"Service call failed: {e}")
        return None  # Explicitly return None if the call fails

if __name__ == "__main__":
    rospy.init_node('proximity_sensor_client')  # Initialize the ROS node
    print("Requesting proximity sensor status...")

    detected = proximity_client()
    if detected is None:
        print("Failed to communicate with the server.")
    elif detected:
        print("Object terdeteksi!")
    else:
        print("Tidak ada objek terdeteksi.")
