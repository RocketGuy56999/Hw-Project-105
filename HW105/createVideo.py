import os
import cv2
path="./assets/Images"
images=[]
for i in os.listdir(path):
    name,ext=os.path.splitext(i)
    if(ext in['.gif', '.png', '.jpg', '.img',]):
        fileName=path+'/'+i
        images.append(fileName)
count=len(images)
frame=cv2.imread(images[0])
height,width,layers=frame.shape
size=(width,height)
out=cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()

