import os
from PIL import Image

im_path = "./images/"
output_path = "./out/"

# For effective GIF
# Images should be the same size
def createGIF():
    output_name = input("Enter out name: ")
    output_speed = input("Enter speed of animation in milliseconds: ")
    output_loop = input("Enter loop type:") # 0 <= number <= 65535
    # 0 infinite, 1 and greater is limited looping

    im_list = os.listdir(im_path)

    ims = [Image.open(im_path + filename) for filename in im_list] # assuming all are images

    ims[0].save(output_path + output_name + ".gif", save_all=True, append_images=ims[1:], duration=float(output_speed), loop=int(output_loop))


    


    

createGIF()