#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import UltrasonicService, UltrasonicServiceResponse
import serial

# Konfigurasi port serial
SERIAL_PORT = '/dev/ttyUSB0'  # Sesuaikan dengan port sensor Anda
BAUD_RATE = 9600

def handle_ultrasonic_request(req):
    try:
        # Membuka koneksi serial
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            ser.flushInput()

            # Membaca data dari sensor
            raw_data = ser.readline().decode('utf-8').strip()

            # Validasi data
            if raw_data.isdigit():
                raw_distance_in_inches = float(raw_data)
                rospy.loginfo(f"Raw distance in inches: {raw_distance_in_inches}")
                return UltrasonicServiceResponse(raw_distance_in_inches)
            else:
                rospy.logwarn("Received invalid data from sensor.")
                return UltrasonicServiceResponse(-1.0)  # -1.0 menandakan error
    except serial.SerialException as e:
        rospy.logerr(f"Serial error: {e}")
        return UltrasonicServiceResponse(-1.0)

def ultrasonic_server():
    rospy.init_node('ultrasonic_server')
    rospy.Service('get_ultrasonic_data', UltrasonicService, handle_ultrasonic_request)
    rospy.loginfo("Ultrasonic server is ready to receive requests.")
    rospy.spin()

if __name__ == "__main__":
    ultrasonic_server()
