__author__ = "KLSA"
__copyright__ = "Copyright 2023 to Infinity and Beyond, CEDES AG"

import cv2
from image_proc.image_proc import ImageProcessor
from visualizer.visualizer import Visualizer
from Logger.logger import csvlogger


class App:
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.visualizer = Visualizer("MyVis")

    def run(self):
        pattern_list = []
        image = cv2.imread("assets/test_image.JPG", cv2.IMREAD_COLOR)
        try:
            while True:
                
                crop = cv2.selectROI("Select the area", image)
                frame = image[int(crop[1]):int(crop[1]+crop[3]), int(crop[0]):int(crop[0]+crop[2])]
                pattern_list = self.image_processor.process(frame)
                
                for pattern in pattern_list:
                    print(f"Pattern name: {pattern.name}, Color: {pattern.color}")
                    csvlogger.logs_p([f"Pattern name: {pattern.name}| Color: {pattern.color}"])
                self.visualizer.visualize(frame, pattern_list)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        except KeyboardInterrupt:
            pass
        finally:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    app = App()
    app.run()
