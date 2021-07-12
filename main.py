import cv2 as cv
import cvlib

# Captura a primeira Webcam no computador, você também pode passar um path relativo para um vídeo.
cap = cv.VideoCapture(0)

def resizeFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isThereFrames, frame = cap.read()

    if isThereFrames == False:
        print("Sem mais frames, terminando o programa.")
        break

    # Redimensiona o frame para 75% para diminuir o uso de recursos e também acelerar a detecção
    frame = resizeFrame(frame)

    # Detecta os rostos presentes e retornar coordenadas deles.
    faces, conf = cvlib.detect_face(frame)

    for face in faces:
        (startX, startY, endX, endY) = face[0], face[1], face[2], face[3]

        # Desenhe um retângulo no frame com a cor verde.
        cv.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0)) 


    cv.imshow("Detectando rostos!", frame)

    # Se a tecla "D" for pressionada, termine o programa.
    if cv.waitKey(20) & 0xFF == ord("d"): 
        break

cap.release()
cv.destroyAllWindows()
cv.waitKey(0)