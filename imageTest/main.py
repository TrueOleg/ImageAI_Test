from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

print("1")
detector = ObjectDetection()
print("2")
detector.setModelTypeAsYOLOv3()
print("3")
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
print("4")
detector.loadModel()
print("5")
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "333.jpg"), output_image_path=os.path.join(execution_path , "144421.jpg"), minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")