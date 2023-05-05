import os
#import cv2
import numpy as np
cimport numpy as cnp
cimport libc.stdlib
import time
from pyvips import Image
# from libcpp.string cimport string


# def zfill_cython(str s, int width):
#     cdef int diff = width - len(s)
#     if diff > 0:
#         return '0' * diff + s
#     else:
#         return s


cdef int height = 4096
cdef int width = 3000
ctypedef cnp.uint8_t DTYPE_t

def save_buffer_img(DTYPE_t[:] pbuffer, int cur_x, int cur_y, str file_path):
    """这是一个扩展模块"""
    
    filename = "{}_{}.bmp".format(str(cur_x).zfill(3), str(cur_y).zfill(3))
    full_filename = file_path + "/captures/" + filename
    if os.path.exists(full_filename):
        return

    start = time.perf_counter()
    cvImage = np.array(pbuffer, copy=False).reshape(width, height, 3)
    end1 = time.perf_counter()
    #cvImage = cnp.frombuffer(pbuffer, dtype=cnp.uint8_t).reshape(height, width, 3)
    print("array reshape cost {}s".format(end1-start))
    #cvImage = cv2.rotate(cv2.flip(cvImage, 1), cv2.ROTATE_90_CLOCKWISE)
    cvImage = cvImage[:, ::-1]
    cvImage = np.transpose(cvImage[::-1, ...][:, ::-1], axes=(1, 0, 2))[::-1, ...]
    end2 = time.perf_counter()
    print("flip rotate cost {}s".format(end2-end1))
    # cv2.imwrite(full_filename, cvImage, [cv2.IMWRITE_JPEG_QUALITY, 80])
    # img = Image.fromarray(cvImage)
    # img.save(full_filename, optimize=True, compress_level=5)
    image = Image.new_from_array(cvImage)
    image.write_to_file(full_filename)

    #np.save(full_filename, cvImage)
    end3 = time.perf_counter()
    print("imwrite cost {}s".format(end3-end2))

