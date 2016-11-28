import socket
server = socket.socket() 
server.connect(("192.168.43.1", 50000))

received_data = server.recv(2048)
# print(received_data.decode('utf-8'))
server.close()

received_data_str = received_data.decode('utf-8')
gps_data_array = str(received_data_str).split('\r')

lat = 0
long = 0
lat_direction = ''
long_direction = ''

for gps_data in gps_data_array:
    if gps_data.startswith('$GPGGA'):
        GPGGA = gps_data.split(',')
        print(GPGGA)

        lat = float(GPGGA[2][0:2]) + float(GPGGA[2][2:])/60
        lat_direction = GPGGA[3]
        print(lat, lat_direction)

        long = float(GPGGA[4][0:3]) + float(GPGGA[4][3:])/60
        long_direction = GPGGA[5]
        print(long, long_direction)

if lat_direction is 'S':
    lat *= -1
if long_direction is 'W':
    long *= -1

gmaps_url = 'http://maps.google.com/maps?q=' + str(lat) +','+ str(long)
print(gmaps_url)