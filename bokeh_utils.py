import os
import cv2
import numpy as np


def get_filename(path):
    return '_'.join(path.replace('\\', '/').split('/')[-1].split('.')[:-1])


def get_image_format(image_path):
    return image_path.split('.')[-1]


def prepare_kernel(path, kernel_side_size):
    kernel_dim = (kernel_side_size, kernel_side_size)
    black, white = 0, 255
    color_threshold = (black + white) // 2
    kernel = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    kernel = cv2.resize(kernel, kernel_dim)
    kernel[np.greater(kernel, color_threshold)] = white
    kernel[np.logical_not(np.greater(kernel, color_threshold))] = black
    return kernel


def prepare_image(path, kernel_side_size):
    image = cv2.imread(path, 1) / 255
    row_pad_left = row_pad_right = col_pad_top = col_pad_bottom = kernel_side_size // 2
    frame_dim = ((row_pad_left, row_pad_right), (col_pad_top, col_pad_bottom), (0, 0))
    image = np.pad(image, frame_dim, "constant")
    return (image, frame_dim)


def do_channel_bokeh(channel, kernel, frame_dim):
    kernel = np.flipud(kernel)
    channel_bokeh = np.zeros((channel.shape[0] - sum(frame_dim[0]), channel.shape[1] - sum(frame_dim[1])))
    for row in range(channel.shape[0] - kernel.shape[0] + 1):
        for col in range(channel.shape[1] - kernel.shape[1] + 1):
            img_slice = channel[row: kernel.shape[0] + row, col: kernel.shape[1] + col]
            product = np.sum(img_slice * kernel) / np.sum(kernel)
            channel_bokeh[row, col] = product * 255
    return channel_bokeh


def save_bokeh(image_bokeh,
               original_image_path,
               kernel_filename,
               kernel_size,
               save_directory=os.path.abspath(os.getcwd())):
    save_name = get_filename(original_image_path)
    image_format = get_image_format(original_image_path)
    addition_to_name = f'{kernel_filename}_{kernel_size}'
    save_directory = save_directory.replace('\\', '/')
    if save_directory[-1] == '/':
        save_directory = save_directory[:-1]
    save_name = f'{save_name}_bokeh_{addition_to_name}.{image_format}'
    save_path = f'{save_directory}/{save_name}'
    cv2.imwrite(save_path, image_bokeh)
    return save_name
