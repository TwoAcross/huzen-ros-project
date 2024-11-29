#!/usr/bin/env python

import rospy
from beginner_tutorials.srv import detectobject

def detect_object_client(threshold):
    rospy.wait_for_service('detect_object')  # Wait for service to be available
    try:
        detect_object = rospy.ServiceProxy('detect_object', detectobject)
        response = detect_object(threshold)
        return response.result
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return "Error"

if __name__ == "__main__":
    rospy.init_node('detect_object_client')  # Initialize ROS node

    # Define threshold value
    threshold = 30.0  # Adjust threshold as needed

    rospy.loginfo(f"Requesting detection with threshold: {threshold} cm")
    result = detect_object_client(threshold)
    rospy.loginfo(f"Detection result: {result}")
