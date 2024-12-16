import rospy
from std_msgs.msg import Float64

def hitung_luas(request):
    diameter = request.data
    jari_jari = diameter / 2
    luas = 3.14159 * (jari_jari ** 2)
    rospy.loginfo(f"Luas tanah untuk diameter {diameter} adalah {luas:.2f} m2")
    return luas

def luas_server():
    rospy.init_node('luas_server')
    s = rospy.Service('hitung_luas', Float64, hitung_luas)
    rospy.loginfo("Server penghitung luas aktif...")
    rospy.spin()

if __name__ == "__main__":
    luas_server()
