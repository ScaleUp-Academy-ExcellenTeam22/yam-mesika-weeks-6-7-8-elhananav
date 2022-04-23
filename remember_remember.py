from PIL import Image


def decode_img(src):
    """
    This function decoding an hidden massage hiding inside of the image pixels.
    Decoding the row number of each black pixel will resolve the hidden massage.
    This function is built on the foundation of:
     "https://stackoverflow.com/questions/56441769/iterate-over-all-pixels-to-check-which-pixels-are-white-and-which-are-black"
    :param src: The path to an image.
    :return: The hidden message.
    """
    img = Image.open(src).convert('RGB')
    pixel = img.load()
    width, height = img.size[0], img.size[1]
    return "".join([chr(j) for i in range(width) for j in range(height) if pixel[i, j] != (255, 255, 255)])


if __name__ == "__main__":
    print(decode_img("resources/code.png"))
