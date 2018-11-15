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