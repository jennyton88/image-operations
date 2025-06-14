# Oct 24, 24

import os
from PIL import Image, ImageOps

im_path = "./images/"
im_output_path = "./out/"
im_file_type = "png"

def createImage(im_name, im_mode, im_size, im_color):
    im = Image.new(im_mode, im_size, im_color)
    im.save(im_output_path + im_name + "." + im_file_type, im_file_type)

# Scale Factor > 0
def scaleImage():
    im_to_scale = input("Enter image name to scale: ")

    try:
        with Image.open(im_path + im_to_scale + "." + im_file_type) as im:
            im_scale_factor = input("Enter scale factor: ")
            scale_im = ImageOps.scale(im, float(im_scale_factor), Image.Resampling.NEAREST) # working with sharp pixels so it's fine to use NEAREST filter
            im_output_name = input("Enter output image name: ")

            while(os.path.isfile(im_output_path + im_output_name + "." + im_file_type)):
                user_check_overwrite = input(f"Do you want to overwrite the file \"{im_output_name }.{im_file_type}\" at this location? [y/quit/any key to change name]: ")
                if (user_check_overwrite == 'y'):
                    scale_im.save(im_output_path + im_output_name + "." + im_file_type, im_file_type)
                    print("Scaled image!")
                    return
                elif (user_check_overwrite == 'quit'):
                    print("Image not saved.")
                    return
                else: # any key
                    print("Please enter a unique name!")
                    im_output_name = input("Enter output image name: ")
                
            scale_im.save(im_output_path + im_output_name + "." + im_file_type, im_file_type)
            print("Scaled image!")
    except OSError:
        print("Not a recognizable image.")

# createImage("test", "RGBA", (1024, 1024), (0,0,0))
scaleImage()