#!/usr/bin/env python

import rospy
from beginner_tutorials.srv import detectobject, detectobjectResponse
import serial

def handle_detect_object(req):
    try:
        # Hubungkan ke sensor MaxBotix MB1403 HRUSB melalui USB
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Ganti port jika berbeda
        raw_data = ser.readline().decode('utf-8').strip()  # Baca data sensor dalam inci
        ser.close()

        # Konversi data dari inci ke cm (1 inci = 2.54 cm)
        distance_in_inches = float(raw_data)  # Asumsi data sensor dalam inci
        distance_in_cm = distance_in_inches * 2.54  # Mengonversi inci ke cm

        # Tampilkan informasi jarak dan threshold di server
        rospy.loginfo(f"Distance: {distance_in_cm} cm, Threshold: {req.threshold} cm")

        # Tentukan hasil berdasarkan threshold dan kirim ke client
        result = "ada objek" if distance_in_cm <= req.threshold else "tidak ada objek"

        return detectobjectResponse(result)

    except Exception as e:
        rospy.logerr(f"Error reading sensor: {e}")
        return detectobjectResponse("Error")

def detect_object_server():
    rospy.init_node('detectobject_server')  # Inisialisasi node
    service = rospy.Service('detect_object', detectobject, handle_detect_object)
    rospy.loginfo("Detect Object Server is ready.")
    rospy.spin()

if __name__ == "__main__":
    detect_object_server()
