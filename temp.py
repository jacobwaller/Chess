from NeuralNet import NeuralNet
import random
import numpy as np
import cv2
import math
import imageio


def tanh(sum): 
    return np.tanh(sum)

def cos(sum):
    return np.cos(sum)

def sin(sum):
    return np.sin(sum)

def tan(sum):
    return np.tan(sum)

def relu(sum):
    if sum>0:
        return 1

    return 0

picWidth = 1920 
picHeight = 1080
mult = 100 #For more frames per loop, increase
reducer = 25 #For more variation, decrease




nn = NeuralNet([4,8,6,4,3], [relu,cos,tanh,sin,tanh])




#let's create a 6 x 6 matrix with all pixels in black color
img = np.zeros((picHeight,picWidth,3),np.uint8)

#let's use "for" cycle to change colorspace of pixel in a random way
# for trans in range(0,100):
for x in range(picHeight):
    print("row",x,"done")
    for y in range(picWidth):
        #We use "0" for black color (do nothing) and "1" for white color (change pixel value to [255,255,255])
        res = nn.predit([x/reducer,y/reducer,0])
        red = (res[0].value+1)*100
        green = (res[1].value+1)*100
        blue = (res[2].value+1)*100 
        
        img[x,y] = [red,green,blue]

    # cv2.imwrite("",img)
#save our image as a "png" image
cv2.imwrite("sample.png",img)

input("Press enter to continue")

cnt = 0

with imageio.get_writer('movie.gif', mode='I', duration=0.05) as writer:
    for t in range(0,int(2 * math.pi * mult)):
        for x in range(picHeight):
            print("row",x,"of picture",t, "of", int(2*math.pi*mult),"done")
            for y in range(picWidth):
                #We use "0" for black color (do nothing) and "1" for white color (change pixel value to [255,255,255])
                res = nn.predit([x/reducer,y/reducer,5*np.sin(t/mult),5*np.cos(t/mult)])
                red = (res[0].value+1)*100
                green = (res[1].value+1)*100
                blue = (res[2].value+1)*100
                
                img[x,y] = [red,green,blue]

        filename = "pics/"+str(cnt)+".png"
        cv2.imwrite(filename,img)
        image = imageio.imread(filename)
        writer.append_data(image)
        cnt += 1


        





