import serial
if __name__ == '__main__':
    estado = ""
    contador_play_pause = 0
    #contador_boton_on_off = 0
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line =ser.readline().decode('utf-8').rstrip()
            if (line == "0xFFA25D"):
                contador_boton_on_off += 1 
                if  contador_boton_on_off%2 == 0:
                    estado = "apagado"
                else:
                    estado = "encendido"
            elif (line == "0xFFE21D"):
                estado = "silenciar"
            elif (line == "0xFF22DD"):
                contador_play_pause += 1 
                if  contador_play_pause%2 == 0:
                    estado = "pausa"
                else:
                    estado = "play"
            elif (line == "0xFF02FD"):
                estado = "rebobinar"
            elif (line == "0xFFC23D"):
                estado = "adelantar"
            elif (line == "0xFF906F"):
                estado = "subir_volumen"
            elif (line == "0xFFA857"):
                estado = "bajar_volumen"
            elif (line == "0xFF9867"):
                estado = "shuffle"
            else:
                print (" Intenta nuevamente")
            print (estado)
            
            

