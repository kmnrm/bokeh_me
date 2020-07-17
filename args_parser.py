import os
import argparse

DESCRIPTION = "This program puts a bokeh effect on an image." \
              "User chooses the kernel picture and the image to use bokeh effect on." \
              "Image has three channels (RGB). Each channel goes through pixel overlaying." \
              "Kernel is a black and white picture, that overlays source image channel's pixels."


def dir_path(path):
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"{path} is not a valid path")
    if os.access(path, os.W_OK):
        return path
    else:
        raise Exception(f":{path} is not writeable")


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle


def parse_arguments():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('image_path',
                        type=lambda x: is_valid_file(parser, x),
                        help='The path of the image to process.')
    parser.add_argument('kernel_path',
                        type=lambda x: is_valid_file(parser, x),
                        help='The path of the image to process.')
    parser.add_argument('kernel_side_size', type=int,
                        help='The width (columns number) and length (rows number) of the kernel.')
    parser.add_argument('--save_to_folder', type=dir_path, help='Set bokeh image save path.')
    return parser.parse_args()
