import numpy as np
from PIL import Image
# import matplotlib.pyplot as plt

def compress_image_svd(path_input_image, ratioOfCompression, fingerprintSeed):
    img = Image.open(path_input_image)
    img_array = np.array(img)

    red, green, blue = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]

    for channel in [red, green, blue]:
        U, S, Vt = np.linalg.svd(channel, full_matrices=False)
        b = int((ratioOfCompression/100) * min(channel.shape))
        S = np.diag(S)
        compressed_channel = U[:, :b] @ S[:b, :b] @ Vt[:b, :]
        
        compressed_channel += fingerprintSeed
        compressed_channel = np.clip(compressed_channel,0,255)

        channel[:] = compressed_channel

    compressed_img_array = np.stack([red, green, blue], axis=-1)

    compressed_img = Image.fromarray(compressed_img_array)

    compressed_image_path = "compressed_image.jpg"
    compressed_img.save(compressed_image_path)

    return compressed_image_path

path_input_image = "/home/garvit-dadheech/Downloads/puppycute.jpg"
ratioOfCompression = int(input("Enter the ratio of compression you want (0-100 in percentage): "))
fingerprintSeed = int(input("Enter a seed for the fingerprint (integer): "))

compressed_image_path = compress_image_svd(path_input_image, ratioOfCompression, fingerprintSeed)
print("Compressed image saved at:", compressed_image_path)



