import rospy
from std_msgs.msg import Float64
from ros_service_name.srv import hitung_luas

def hitung_insentif(diameter):
    rospy.wait_for_service('hitung_luas')
    try:
        hitung_luas = rospy.ServiceProxy('hitung_luas', Float64)
        luas = hitung_luas(diameter).data
        insentif = luas * 150000
        rospy.loginfo(f"Insentif yang diperoleh: Rp {insentif:.2f}")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service hitung_luas gagal: {e}")

if __name__ == "__main__":
    rospy.init_node('insentif_client')
    diameter = 120.0  # Sesuaikan dengan diameter tanah
    hitung_insentif(diameter)
