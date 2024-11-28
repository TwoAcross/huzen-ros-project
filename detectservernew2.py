import serial

def read_sensor_data(port='/dev/ttyUSB0', baudrate=9600):
    try:
        # Membuka port serial dan menghubungkan ke sensor
        ser = serial.Serial(port, baudrate, timeout=1)
        print("Connected to sensor at", port)
        
        while True:
            # Membaca satu baris data dari sensor
            data = ser.readline().decode('utf-8').strip()
            if data:
                print("Raw Data:", data)  # Menampilkan data mentah yang diterima
    except serial.SerialException as e:
        print("Error connecting to sensor:", e)

if __name__ == "__main__":
    read_sensor_data()
