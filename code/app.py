__author__ = "KLSA"
__copyright__ = "Copyright 2023 to Infinity and Beyond, CEDES AG"

import cv2
import numpy as np
from image_proc.image_proc import ImageProcessor
from visualizer.visualizer import Visualizer
from Logger.logger import csvlogger
from Camera.camera import Camera


class App:
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.visualizer = Visualizer("MyVis")
        self.camera = Camera()
    
    def run(self):

        try:
            while cv2.waitKey(1) & 0xFF != ord("q"): #Läuft bis 'q' gedrückt wird
                image = self.camera.capture_frame() #Bild aufnehmen

                if cv2.waitKey(1) & 0xFF == ord("c"):  #Wird 'c' gedrückt kann das Bild zugeschnitten werden

                    crop = cv2.selectROI("Select the area", image) #Bild zuschneiden, mit space bestätigen
                    
                    cv2.destroyAllWindows()    #fenster schliessen
                    
                    frame = image[int(crop[1]):int(crop[1]+crop[3]), int(crop[0]):int(crop[0]+crop[2])] #Bild zuschneiden
                    frame = cv2.copyMakeBorder(frame, 100, 100, 100, 100, cv2.BORDER_CONSTANT)  #Rahmen um Bild legen
                    pattern_list = self.image_processor.process(frame)  #Bild an image prozessor übergeben
                    
                    for pattern in pattern_list:    #alle Formen finden, ausgeben und anzeigen
                        print(f"Pattern name: {pattern.name}, Color: {pattern.color}")
                        csvlogger.logs_p([f"Pattern name: {pattern.name}| Color: {pattern.color}"]) #Gefundene Formen und Farben an CSV logger übergeben
                        self.visualizer.visualize(frame, pattern_list)  #Bild mit umrandeten Formen anzeigen

                cv2.imshow("Kamera", image) #Kamerabild anzeigen
                cv2.resizeWindow("Kamera", 1080, 720)   #Fenster auf Fixe Grösse anpassen
                
                if cv2.waitKey(1) & 0xFF == ord("q"):   #Wenn 'q' gedrückt -> break
                    break
        except KeyboardInterrupt:
            pass
        finally:
            cv2.destroyAllWindows() #Alle Fenster schliessen


if __name__ == "__main__":
    app = App()
    app.run()