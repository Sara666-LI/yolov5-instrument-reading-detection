import detect_holes
import detect_panel
import detect_monitor
import time
import detect_meter

#detect the holes on the centrifugeL: depth as input
print(detect_holes.detect(0.3))

#detect panel on the centrifuge
#print(detect_panel.detect())

#detect the monitor on the oven
#print(detect_monitor.detect())

#detect the meter on the oven
##print(detect_meter.detect())

time.sleep(5)