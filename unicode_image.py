import time
from PIL import Image
# so I need to run this from terminal to get it to work?

img_src = input("What image to use? ")
img_out_name = img_src.split(".")[0] + "_ascii.txt"
threshold = int(input("What is the threshold for brightness? (0 to 255) "))
invert = (input("Invert image? (y/n, default no) ") == "y")

start_time = time.time()

def img_to_dots(img):
    img_size = img.size
    pixels = img.load()
    out_file = open(img_out_name, "w")

    # split up list into 2 by 4 sections
    for row_slice in range(-(-img_size[1] // 4)): # first make slice it into row groups of height 4
        for col_slice in range(-(-img_size[0] // 2)): # this slices it into the individual bits

            # this is the dots string, formatted like input to dots_to_char
            cur_dots = ""
            for x_coord in range(2): # two columns in each slice
                for y_coord in range(4): # four rows in each slice

                    pixel_x, pixel_y = (2 * col_slice + x_coord, 4 * row_slice + y_coord)
                    # if outside of bounds, add a 0 to the pixel.
                    if pixel_x >= img_size[0] or pixel_y >= img_size[1]:
                        cur_dots += "0"
                    else:
                        # get pixel sum
                        pixel_value = sum(pixels[pixel_x, pixel_y]) / 4
                        # add the thing to current dots
                        if (pixel_value > threshold) == invert:
                            cur_dots += "1"
                        else:
                            cur_dots += "0"
            # write the character to the cur_dots.
            out_file.write(dots_to_char(cur_dots))
        out_file.write("\n")

def dots_to_char(dots):
    '''dots is a string of 8 characters that specifies columns in order.'''
    val_ordered_dots = dots[7] + dots[3] + dots[6:3:-1] + dots[2::-1]
    val = int(val_ordered_dots, 2)
    return chr(0x2800 + val)

img_to_dots(Image.open(img_src))
print("Your result is in the file, \"" + img_out_name + "\".")
print("t: " + str(time.time() - start_time))