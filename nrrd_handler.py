import nrrd
import SimpleITK as sitk
import numpy as np


class NrrdHandler:
    """This class decodes the nrrd file with different libraries
    """
    
    def __init__(self, file_path: str):
        """
        Initialize with the file path
        :param file_path: file path
        """
        self.file_path = file_path

    def read_by_pynrrd(self) -> np.ndarray:
        """
        Decode the nrrd file using pynrrd library
        :return: image
        """
        # header has the information of the nrrd file
        img, header = nrrd.read(self.file_path)

        return img

    def read_by_sitk(self) -> np.ndarray:
        """
        Decode the nrrd file using SimpleITK library
        :return: image
        """
        # header has the information of the nrrd file
        header = sitk.ReadImage(self.file_path)
        img = sitk.GetArrayFromImage(header)
        return img
