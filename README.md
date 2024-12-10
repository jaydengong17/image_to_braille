# image_to_braille
This tool converts an image to a text file with braille characters. It maps every pixel in the image to a pixel inside the braille.

# Requirements
Requires [pillow/PIL](https://pypi.org/project/pillow/).

Install:
`pip3 install pillow`

# Example

<img src="./assets/images/test_image.png" alt="test image" width=50px/>

becomes

<p style="line-height: 0.5;">⢹⠁⡯⠁⠪⢅⠈⡏<br>⠈⠀⠉⠁⠈⠁⠀⠁</p>