import rp2
import network
import machine
import socket
from time import sleep_ms

ap = network.WLAN(network.AP_IF)
ap.config(essid="pico_w_ap", password="12345678")
ap.active(True)

led = machine.Pin('LED', machine.Pin.OUT)
led.off()

# HTTP server with socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
print('IP Address To Connect to:: ' + ap.ifconfig()[0])
s = socket.socket()
s.bind(addr)
s.listen(10)

print('Listening on', addr)

# Listen for connections
while True:
    try:
        print("yep")
        cl, addr = s.accept()
        led.on()
#        print('Client connected from', addr)
        r = str(cl.recv(1024))
#        print(r)
        r = r[r.find("/"):]
        r = r[1:r.find(" ")]
        if (r == ""):
            r = "index.html"

#        print(r)
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        send_file_buffer_size = 1024
        with open(r, 'rb') as file:
            while True:
                buf = file.read(send_file_buffer_size)
                if len(buf):
                    cl.send(buf)
                if len(buf) < send_file_buffer_size:
                    break;
        sleep_ms(100)
        cl.close()
        led.off()
        
    except OSError as e:
        cl.close()
#        print('Connection closed')
        led.off()
