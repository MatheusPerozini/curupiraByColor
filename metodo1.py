import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture(0)

time.sleep(2)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    # RET É UM BOOLEAN QUE RETORNA FALSE SE NÃO ESTIVER CAPTURANDO OU SE VIDEO ACACABOU
    # FRAME É OS FRAMES QUE PODEMOS ALTERAR
    ret, frame = cap.read()
    #COLOCAR BLUR QUE AJUDA A NÃO DISTORCER A IMAGEM
    blur = cv.GaussianBlur(frame , (15 , 15) , 0)
    #COLOCAR A IMAGEM EM COR HSV
    hsv = cv.cvtColor(blur , cv.COLOR_BGR2HSV)
    #SÃO OS MAXIMO DE COR QUE ELE ACEITA E O MENOR COR QUE ACEITA
    lower = [18 , 50 , 50]
    upper = [35 , 255 , 255]
    #TRANSFORMA O ARRAY EM NUMERO COM O NUMPY
    lower = np.array(lower , dtype='uint8')
    upper = np.array(upper , dtype='uint8')
    #APLICA OS FILTROS
    mask = cv.inRange(hsv , lower , upper)
    #APLICA OS EFEITOS NO FRAME , COMBINANDO COM A MASK
    output = cv.bitwise_and(frame , hsv , mask=mask)
    #AKI ELE IRA CONTA O TAMANHO DO FOGO POR PIXEIS QUE NÃO SAO ZERO
    tamanhoFogo = cv.countNonZero(mask)
    #SE O TAMANHO QUE ELE CONTA FOR MAIOR QUE NUMERO ELE VAI MOSTRAR QUE DETECTOU
    if int(tamanhoFogo) > 15000 :
        print("FOGOOOOO AAAA")

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame
    cv.imshow('DETECTA FOGO PELA COR', output)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
