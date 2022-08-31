import os

from typing import Union
from PIL import Image


def __fetch_image(
    self, src_img: Union[str, Image.Image], gif_allowed: bool
) -> Image.Image:

    if isinstance(src_img, str) and (gif_allowed or not src_img.endswith(".gif")):

        # Sanity Check if the path exists
        if not os.path.isfile(src_img):
            raise FileNotFoundError("Path not found")
        try:
            # Open the image at given path
            img = self.__open_image(src_img)
        except:
            # File is not an Image
            raise Exception("Wrong format")
    elif isinstance(src_img, Image.Image) and (
        gif_allowed or not self.__isgif(src_img)
    ):

        if src_img.format == "GIF":
            # Do not convert GIF file
            return src_img
        elif src_img.format == "PNG":
            # Convert the Image to RGBA if it's png
            img = src_img.convert("RGBA")
        else:
            # Otherwise convert it to RGB
            img = src_img.convert("RGB")
    else:
        # File is not an Image
        # OR it's a GIF but GIF is not allowed

        # Raise the GENERIC exception here
        raise Exception("Wrong format")
    return img
