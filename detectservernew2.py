import serial

def read_sensor_data(port='/dev/ttyUSB0', baudrate=9600):
    try:
        ser = serial.Serial(port, baudrate, timeout=2)  # Gunakan timeout lebih lama
        print("Connected to sensor at", port)
        
        while True:
            ser.write(b'R')  # Kirim trigger jika diperlukan (coba hapus jika tidak perlu)
            data = ser.readline().decode('utf-8').strip()  # Baca data dari sensor
            
            if data:
                print("Raw Data:", data)  # Tampilkan data mentah
            else:
                print("No data received, check sensor connection or configuration.")
    except serial.SerialException as e:
        print("Error connecting to sensor:", e)

if __name__ == "__main__":
    read_sensor_data()
