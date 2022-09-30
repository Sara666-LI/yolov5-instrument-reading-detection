import numpy as np
import cv2
import torch
import os

#label_path = 'C:/Users/Sara/Documents/detection/yolov5/runs/detect/exp389_panel_real_390labels/labels/'
#image_path = 'C:/Users/Sara/Documents/detection/yolov5/runs/detect/exp389_panel_real_390labels/images'
label_path = 'C:/Users/Sara/Documents/detection/yolov5/data/test_label/'
image_path = 'C:/Users/Sara/Documents/detection/yolov5/data/test/'
##label_path = 'C:/Users/Sara/Desktop/few-shot_conf0.9Detectlabels/labels/'
##image_path = 'C:/Users/Sara/Desktop/few-shot_conf0.9Detectlabels/images/'

#坐标转换，原始存储的是YOLOv5格式
# Convert nx4 boxes from [x, y, w, h] normalized to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
def xywhn2xyxy(x, w=1280, h=720, padw=0, padh=0):

    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = w * (x[:, 0] - x[:, 2] / 2) + padw  # top left x
    y[:, 1] = h * (x[:, 1] - x[:, 3] / 2) + padh  # top left y
    y[:, 2] = w * (x[:, 0] + x[:, 2] / 2) + padw  # bottom right x
    y[:, 3] = h * (x[:, 1] + x[:, 3] / 2) + padh  # bottom right y
    return y

class_true = []   
count = 0 
folder = os.path.exists('GT')
if not folder:           
	os.makedirs('GT') 
	
folderlist = os.listdir(label_path)
for i in folderlist:
    label_path_new = os.path.join(label_path,i)
    count += 1
    print("count:", count)
    if (count<390):
       with open(label_path_new, 'r') as f:
           lb = np.array([x.split() for x in f.read().strip().splitlines()], dtype=np.float32)  # labels
        
    read_label = label_path_new.replace(".txt", ".png")
    read_label_path = read_label.replace('test_label', 'test')
    print(read_label_path)
    img = cv2.imread(str(read_label_path))
    #h, w = img.shape[:2]
    print(lb[:, 0])
    class_true.append(lb[:, 0].tolist())
#print(class_true)
print("class_true shape:", len(class_true))

print("class 0 count:", sum(row.count(0.0) for row in class_true))
print("class 1 count:", sum(row.count(1.0) for row in class_true))
print("class 2 count:", sum(row.count(2.0) for row in class_true))
print("class 3 count:", sum(row.count(3.0) for row in class_true))
print("class 4 count:", sum(row.count(4.0) for row in class_true))
print("class 5 count:", sum(row.count(5.0) for row in class_true))
print("class 6 count:", sum(row.count(6.0) for row in class_true))
print("class 7 count:", sum(row.count(7.0) for row in class_true))
print("class 8 count:", sum(row.count(8.0) for row in class_true))
print("class 9 count:", sum(row.count(9.0) for row in class_true))
    #for i in range(lb.shape[0]):
    #    lb[i, 1:] = xywhn2xyxy(lb[i, 1:], w, h, 0, 0)  # 反归一化
    #    print(lb)
    #lb[:, 1:] = xywhn2xyxy(lb[:, 1:], w, h, 0, 0)  # 反归一化
    #print("lb_shape:", lb.shape)
    #for _, x in enumerate(lb):
    #    class_label = int(x[0])  # class
    #    cv2.rectangle(img, (int(x[1]), int(x[2])), (int(x[3]), int(x[4])), (0, 255, 0))
    #    with open('GT/' + i, 'a') as fw:
    #        fw.write('0' + ' ' + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + ' ' + str(
    #            x[4]) + '\n')
