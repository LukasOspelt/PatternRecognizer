import cv2

class Camera:
    #Klasse initialisieren mit Kameraindex, 0 = Frontkamera, 1 = Rückkamera
    def __init__(self, camera_index=1):
        self.camera_index = camera_index
        self.capture = cv2.VideoCapture(self.camera_index)

    #Methode um Kamera zu öffnen
    def open(self):
        if not self.capture.isOpened():
            self.capture.open(self.camera_index)

    #Methode zum Bild aufnehmen
    def capture_frame(self):
        self.open()
        if self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                return frame
            else:
                print("Error capturing frame.")
                return None
        else:
            print("Error opening camera.")
            return None

    #Kamera freigeben wenn fertig
    def release(self):
        if self.capture.isOpened():
            self.capture.release()

    #Destruktor
    def __del__(self):
        self.release()

if __name__ == "__main__":
    camera = Camera()
    frame = camera.capture_frame()
    if frame is not None:
        cv2.imshow('Camera', frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
