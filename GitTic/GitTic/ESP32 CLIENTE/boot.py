import esp
import time
esp.osdebug(None)
print("INICIO DE PROGRAMA")
def do_connect(essid, passw):
    import network
    sta_if = network.WLAN(network.STA_IF)
    print("CONEXIONA A: ",essid)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, passw)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
do_connect("Invitado", "1a2s3d4f5")
def http_get(host, path):
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close