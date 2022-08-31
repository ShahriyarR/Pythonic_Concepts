import os

from typing import Union
from PIL import Image
from collections import defaultdict


def __open_image(src_img: str) -> Image.Image:
    ...

def __isgif(src_img: Image.Image) -> bool:
    ...

def _get_opened_image(src_img: str) -> Image.Image:
    # Sanity Check if the path exists
    if not os.path.isfile(src_img):
        raise FileNotFoundError("Path not found")
    try:
        # Open the image at given path
        img = __open_image(src_img)
    except:
        # File is not an Image
        raise Exception("Wrong format")
    else:
        return img

def _get_img_converted_to_rgb_or_rgba(src_img: Image.Image) -> Image.Image:

    _map = defaultdict(lambda: lambda: src_img.convert("RGB"))
    _map["PNG"] = lambda: src_img.convert("RGBA")
    _map["GIF"] = lambda: src_img
    return _map[src_img.format]()



def __fetch_image(
    self, src_img: Union[str, Image.Image], gif_allowed: bool
) -> Image.Image:

    if isinstance(src_img, str) and (gif_allowed or not src_img.endswith(".gif")):

        return _get_opened_image(src_img=src_img)

    elif isinstance(src_img, Image.Image) and (
        gif_allowed or not __isgif(src_img)
    ):
        
        return _get_img_converted_to_rgb_or_rgba(src_img=src_img)

    
    raise Exception("Wrong format")
