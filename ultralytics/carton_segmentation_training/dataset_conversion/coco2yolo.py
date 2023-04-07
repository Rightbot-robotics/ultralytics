import json
import os

train_images_dir = '/home/bhavya/Projects/YOLOv8/coco_carton/oneclass_carton/images/train'  
val_images_dir = '/home/bhavya/Projects/YOLOv8/coco_carton/oneclass_carton/images/val'
train_json_dir = '/home/bhavya/Projects/YOLOv8/annotations/instances_train2017.json'
val_json_dir = '/home/bhavya/Projects/YOLOv8/annotations/instances_val2017.json'
train_labels_dir = '/home/bhavya/Projects/YOLOv8/coco_carton/oneclass_carton/labels/train/'
val_labels_dir = '/home/bhavya/Projects/YOLOv8/coco_carton/oneclass_carton/labels/val/'

images_list = os.listdir(train_images_dir) #path of the images directory

json_file = open(train_json_dir) #path of the labels (corresponding images) directory
json_data = json.load(json_file)
json_file.close()

def get_anotations(json_data, img_id):
    i = 0
    annotations = []
    for annotation in json_data['annotations']:
        if annotation['image_id'] == img_id:
            annotations.append(annotation['bbox'])
            i+=1
    return annotations, i
category_id = 0 #only box class in this case
for image in images_list:
    for files in json_data['images']:
        if files['file_name'] == image:
            img_file_name = image.split('.')[0]
            img_id = files['id']
            W = files['width']
            H = files['height']
            annotations, i = get_anotations(json_data, img_id)   

            file_object = open(f"{train_labels_dir}{img_file_name}.txt", "w") #replace {tain_labels_dir} to the path to save yolo labels

            for annotation in annotations:
                x = annotation[0]
                y = annotation[1]
                w = annotation[2]
                h = annotation[3]

                x_centre = (x + (x+w))/2
                y_centre = (y + (y+h))/2

                x_centre = x_centre / W
                y_centre = y_centre / H
                w = w / W
                h = h / H

                x_centre = format(x_centre, '.6f')
                y_centre = format(y_centre, '.6f')
                w = format(w, '.6f')
                h = format(h, '.6f')
          
                file_object.write(f"{category_id} {x_centre} {y_centre} {w} {h}\n")

            file_object.close()





