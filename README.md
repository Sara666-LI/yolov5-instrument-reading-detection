# yolov5-instrument-reading-detection
This is an implementation of instrument reading detection on Python 3 and YOLOv5 which can be applied to many scenarios like warehouse management, industrial automation and robotics. 
Before the application, you may need to read the official information about the deployment of YOLOv5. https://github.com/ultralytics/yolov5

If you use Docker, the code has been verified to work on this Docker container! https://hub.docker.com/r/ultralytics/yolov5

For the annotation tool, please refer to labelImg 

Specific ackages may needed, install by:
pip install -r requirements.txt

1. To call detection functions, first import:

import detect_holes
import detect_panel
import detect_monitor
import detect_meter
#from ipynb.fs.full.meters_reading import detect as detect_meter


2. Then call functions with:

detect_holes.detect(depth)
detect_panel.detect()
detect_monitor.detect()
detect_meter.detect()

(Note: "detect_holes" and "detect_panel" are for the centrifuge. The rest are for the other machine)


3. Outputs:


![image](https://user-images.githubusercontent.com/49709009/192931399-e1b48811-4400-4c98-bff2-f99c06b8ab78.png)
detect_holes.detect(depth):

[x, y, z]

(Note:the method above for 3D coordinates is only for reference, you should have your own idea. 
To only get the pixel coordinates, you should comment the line 202:result = rs.rs2_deproject_pixel_to_point(color_intrin, [x,y], depth))

![image](https://user-images.githubusercontent.com/49709009/192944760-88edd3be-a2ab-40f4-8d40-a873a9e317ea.png)

detect_panel.detect():

[ListOfButton], [ListOfDigits]

example: (['power_on', 'open_on'], [0, 230, 1])
(Note: "open_on" and "open_off" indicate that whether the light of the "open" button is on or off, e.g., "open_on" means the light of "open" button is on and the machine is covered. 
"Power_on" and "power_off" indicate that whether power is on or off. 
The status of button "power will go first.)



![image](https://user-images.githubusercontent.com/49709009/192944676-cbea5578-ff24-4188-a191-e26b6e871a3e.png)

detect_monitor.detect():

[CurrentTemperature, TargetTemperature]

example: [97.5, 170.0]
(Note: second element of the output list will be 0.0 if target temperature is not detected
Here in our project, target temperature(the second element) is not in consideration)

![image](https://user-images.githubusercontent.com/49709009/192947580-da10ca00-9e12-4606-8a8d-da3e2bcfbd28.png)

detect_meter.detect():
angles
example: 321.6°

4. camera requirrement:

capture distance-original equipment:
centrifuge holes detection: 20cm
centrifuge panel detection: 27cm
oven monitor detection: 20cm
oven meter detection:17cm

5. For the new oven panel:
Please use the updated detection model best_oven_panel_new.pt
Replace  detec_meter.py with the updated one detec_meter_new.py
Example:
![image](https://user-images.githubusercontent.com/49709009/192932371-36151197-efb0-4157-a1ed-7cb573ff700e.png)



--------------------------------------------------------------------
The repository includes:

    Source code of YOLOv5
    
    Application of labelImg tool
   
    Evaluation on yolo metrics (AP)
    
    Example of detection on my own dataset - LED/LCD instrument and pointer meter reading recognition 
    
    
