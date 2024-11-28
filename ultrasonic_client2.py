#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import UltrasonicService

def request_and_process_data():
    rospy.loginfo("Waiting for the ultrasonic service...")
    rospy.wait_for_service('get_ultrasonic_data')  # Menunggu server layanan tersedia
    try:
        # Membuat proxy untuk memanggil service
        get_ultrasonic_data = rospy.ServiceProxy('get_ultrasonic_data', UltrasonicService)

        rospy.loginfo("Calling the ultrasonic service...")
        # Meminta data dari server
        response = get_ultrasonic_data()

        # Validasi dan konversi data
        if response.raw_data_cm >= 0:
            distance_cm = response.raw_data_cm  # Data sudah dalam cm (disesuaikan)
            rospy.loginfo(f"Distance from ultrasonic sensor: {distance_cm:.2f} cm")
        else:
            rospy.logwarn("Failed to get valid data from the ultrasonic service.")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

if __name__ == "__main__":
    rospy.init_node('ultrasonic_client')  # Inisialisasi node klien ROS
    rospy.loginfo("Ultrasonic client node has started.")
    while not rospy.is_shutdown():
        request_and_process_data()  # Memanggil layanan
        rospy.sleep(1)  # Interval request (1 detik)
