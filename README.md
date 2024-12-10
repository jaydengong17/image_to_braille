# image_to_braille
This tool converts an image to a text file with braille characters. It maps every pixel in the image to a pixel inside the braille.

# Requirements
Requires [pillow/PIL](https://pypi.org/project/pillow/).

Install:
`pip3 install pillow`

# Example

![test image](\assets\images\test_image.png)

becomes

<p style="line-height: 1;">⢹⠁⡯⠁⠪⢅⠈⡏<br>⠈⠀⠉⠁⠈⠁⠀⠁</p>