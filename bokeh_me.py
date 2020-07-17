import os
import logging
from args_parser import parse_arguments
from bokeh_utils import *

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    )


def main():
    args = parse_arguments()
    image_path = args.image_path.name
    kernel_path = args.kernel_path.name
    kernel_side_size = args.kernel_side_size

    save_to = args.save_to_folder if args.save_to_folder else os.path.abspath(os.getcwd())

    kernel = prepare_kernel(kernel_path, kernel_side_size)
    image, frame_dim = prepare_image(image_path, kernel_side_size)
    channels = cv2.split(image)

    logging.info('Processing image...')

    image_bokeh = []
    for step, channel in enumerate(channels):
        channel_bokeh = do_channel_bokeh(channel, kernel, frame_dim)
        image_bokeh.append(channel_bokeh)
        logging.info(f'Channel {step + 1}/3 processed.')

    logging.info('Channels processed.')
    image_bokeh = cv2.merge(image_bokeh).astype(np.uint8)
    kernel_filename = get_filename(kernel_path)

    bokeh_image = save_bokeh(image_bokeh, image_path, kernel_filename, kernel_side_size, save_to)
    logging.info(f'Image {bokeh_image} saved to {save_to}')


if __name__ == '__main__':
    main()
