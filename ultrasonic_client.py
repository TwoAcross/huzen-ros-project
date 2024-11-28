#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import UltrasonicService

def request_and_process_data():
    rospy.wait_for_service('get_ultrasonic_data')
    try:
        # Membuat proxy untuk memanggil service
        get_ultrasonic_data = rospy.ServiceProxy('get_ultrasonic_data', UltrasonicService)

        # Meminta data dari server
        response = get_ultrasonic_data()

        if response.raw_data_cm >= 0:
            # Konversi dari inci ke cm
            distance_cm = response.raw_data_cm * 2.54
            rospy.loginfo(f"Distance in cm: {distance_cm:.2f} cm")
        else:
            rospy.logwarn("Failed to get valid data from server.")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

if __name__ == "__main__":
    rospy.init_node('ultrasonic_client')
    while not rospy.is_shutdown():
        request_and_process_data()
        rospy.sleep(1)  # Interval request (1 detik)
