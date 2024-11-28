#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import detectobject

def detect_object_client(threshold):
    rospy.wait_for_service('detect_object')
    try:
        detect_object = rospy.ServiceProxy('detect_object', detectobject)
        response = detect_object(threshold)
        return response.result
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "%s [threshold]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        threshold = float(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)

    print("Requesting threshold:", threshold)
    result = detect_object_client(threshold)
    print("Server Response:", result)
