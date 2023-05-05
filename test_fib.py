import helper
import cv2
import time

# 我们看到该 pyd 文件直接就被导入了
# 至于中间的 cp38-win_amd64 指的是解释器版本、操作系统等信息
print(helper) 
"""
<module 'fib' from 'D:\\satori\\fib.cp38-win_amd64.pyd'>
"""

# 我们在里面定义了一个 fib 函数
# fib.pyx 里面定义的函数在编译成扩展模块之后可以直接用
# print(helper.zfill_cython('5', 6))  
"""
6765.0
"""

# doc string
img = cv2.imread(r"E:/NeatSvtScanSide/data/20230428_5/captures/000_008.jpg")
bytearray_a = bytearray(img.tobytes())
print(helper.save_buffer_img.__doc__)
start = time.perf_counter()
helper.save_buffer_img(memoryview(bytearray_a), 0, 0, "D:/data")
end = time.perf_counter()
print(f"save_buffer_img cost {end-start} seconds")
"""
这是一个扩展模块
"""