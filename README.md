# bokeh.me
 Make a bokeh effect on your images
 
 ![Source image with lights](screenshots/lights.jpg) 
 ![Triange shaped kernel size 25 bokeh effect](screenshots/lights_bokeh.jpg)

### Getting started
This program puts a bokeh effect on an image. User chooses the kernel picture
and the image to process bokeh effect on. Image has three channels (RGB). Each
channel goes through pixel overlaying. Kernel is a black and white picture,
that overlays source image channel's pixels.

Script `bokeh_me.py` is a script to run. It takes 4 arguments (3 positional and 1 positional):

positional arguments:

 - `image_path` - the path of the image to process.
 - `kernel_path` - the path of the image to process.
 - `kernel_side_size` - the width (columns number) and length (rows number) of the kernel.

optional arguments:
 - `--save_to_folder` - set bokeh image save path.

### How to run

To get your image with bokeh follow the steps below:
1. Clone or download this repository.
2. Go to repository in terminal
3. In terminal run:
```shell script
$ python3 bokeh_me.py <image_path> <kernel_path> <kernel_side_size>
```

For help run:
```shell script
$ python3 bokeh_me.py -h
```

```shell script
$ python3 bokeh_me.py -h
usage: bokeh_me.py [-h] [--save_to_folder SAVE_TO_FOLDER]
                   image_path kernel_path kernel_side_size

This program puts a bokeh effect on an image.User chooses the kernel picture
and the image to use bokeh effect on.Image has three channels (RGB). Each
channel goes through pixel overlaying.Kernel is a black and white picture,
that overlays source image channel's pixels.

positional arguments:
  image_path            The path of the image to process.
  kernel_path           The path of the image to process.
  kernel_side_size      The width (columns number) and length (rows number) of
                        the kernel.

optional arguments:
  -h, --help            show this help message and exit
  --save_to_folder SAVE_TO_FOLDER
                        Set bokeh image save path.
```


#### Examples
![](source_images/blue_lights.jpg)
```shell script
$ python3 bokeh_me.py blue_lights.jpg tri.tif 19 --save_to_folder D:\
```

##### Result:
```shell script
2020-07-18 02:56:44,719 INFO Processing image...
2020-07-18 02:56:50,945 INFO Channel 1/3 processed.
2020-07-18 02:56:57,692 INFO Channel 2/3 processed.
2020-07-18 02:57:04,312 INFO Channel 3/3 processed.
2020-07-18 02:57:04,312 INFO Channels processed.
2020-07-18 02:57:04,327 INFO Image blue_lights_bokeh_tri_19.jpg saved to D:\
```

![](screenshots/blue_lights_bokeh_tri_19.jpg)