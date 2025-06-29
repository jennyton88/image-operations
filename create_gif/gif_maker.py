import os
from PIL import Image

img_path = "./images/"
output_path = "./out/"


def createGIF():
    output_name = input("Enter file name: ")
    output_speed = input("Enter length of GIF: ")
    output_loop = input("Enter loop type (infinite 0 / finite 1): ") 

    loop_type = 0 # default
    if (output_loop == "finite" or output_loop == "1"):
        loop_type = 1
    elif (output_loop == "infinite" or output_loop == "0"):
        loop_type = 0

    img_list = os.listdir(img_path)

    img_names = []
    for file_name in img_list:
        img_names.append(file_name)
    
    img_names.sort()

    # convert to seconds per frame
    loop_speed = (float(output_speed) / len(img_names)) * 1000 # convert to ms

    if (loop_speed > 65535):
        print("Sorry, per frame limit is 65535 ms ")
        return
    
    imgs = []
    for file_name in img_names:
        imgs.append(Image.open(img_path + file_name))

    print("creating gif...")
    imgs[0].save(output_path + output_name + ".gif", save_all=True, append_images=imgs[1:], duration=loop_speed, loop=loop_type)
    print("done!")

    


    

createGIF()