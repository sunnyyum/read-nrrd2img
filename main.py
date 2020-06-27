import argparse
import sys
import nrrd_handler
import matplotlib.pyplot as plt
import numpy as np


def read_opt(args: list) -> argparse.Namespace:
    """
    Read the arguments and store into variable
    Maps the input from command line with variables, based on flag in the command line input.
    :param args: list that contains the argument after python file itself
    :return: an object holding attribute of input file path
    """
    parse = argparse.ArgumentParser(description="extract image from the given nrrd file")

    parse.add_argument('-i', required=True, dest='input_file',
                       help='input path that has the nrrd file')

    return parse.parse_args(args)


if __name__ == '__main__':
    # reading flags from the command line
    opts = read_opt(sys.argv[1::])
    file_path = opts.input_file

    # set the file path
    nH = nrrd_handler.NrrdHandler(file_path)

    # getting the image
    # using two different libraries (pynrrd and SimpleITK)
    img_pynrrd = nH.read_by_pynrrd()
    img_sitk = nH.read_by_sitk()

    # plot two images
    fig, ax = plt.subplots(1, 2)

    if len(img_pynrrd.shape) == 2:
        ax[0].imshow(img_pynrrd)
        ax[1].imshow(img_sitk)
    elif len(img_pynrrd.shape) == 3:
        # if there is only three layer
        # assume color image
        if img_pynrrd.shape[0] == 3:
            img_pynrrd_restacked = np.stack([img_pynrrd[ind, :, :] for ind in range(3)], axis=2)
            ax[0].imshow(img_pynrrd_restacked)
            ax[1].imshow(img_sitk)
        else:
            ax[0].imshow(img_pynrrd[:, :, 0])
            ax[1].imshow(img_sitk[0])

    elif len(img_pynrrd.shape) == 4:
        ax[0].imshow(img_pynrrd[0, :, :, 0])
        ax[1].imshow(img_sitk[0, :, :, 0])

    ax[0].set_title('pynrrd')
    ax[1].set_title('SimpleITK')

    plt.show()
