from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

results = model.train(data="../datasets/oneclass_carton/config.yaml",epochs=50)
