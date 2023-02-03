# -*- encoding=utf8 -*-
__author__ = "Jackin"

import datetime
import pytesseract
from PIL import Image
from airtest.aircv import *
from airtest.core.api import *

auto_setup(__file__)

# set pytesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSDATA_PREFIX = r'C:\Program Files\Tesseract-OCR\tessdata'


def snapshot_and_extract():
    # 局部截图
    now = datetime.datetime.now()
    time_format = now.strftime("%Y%m%d-%H%M%S")
    screen = G.DEVICE.snapshot()
    screenshot = cv2_2_pil(screen)
    screenshot.save(f"D:/workspace_python/tmp/screenshot-{time_format}.png", quality=99, optimize=True)
    local = aircv.crop_image(screen, (40, 190, 390, 320))

    # 保存局部截图到指定文件夹
    pil_image = cv2_2_pil(local)
    pil_image.save("D:/workspace_python/tmp/snapshot-area.png", quality=99, optimize=True)

    # 读取截图并识别截图中的文字
    image = Image.open(r'D:/workspace_python/tmp/snapshot-area.png')
    extracted = pytesseract.image_to_string(image, lang='chi_sim+eng')
    print(f"------------- 识别混合数据\r\n {extracted} \r\n-------------")


def extract_captcha():
    # 读取外部图像，识别验证码
    captcha = Image.open(r'D:/workspace_python/captcha.jpg')
    extracted = pytesseract.image_to_string(captcha)
    print(f"------------- 识别验证码\r\n {extracted} \r\n-------------")


def extract_chinese():
    # 读取外部图像，识别中文
    chinese = Image.open(r'D:/workspace_python/chinese.png')
    extracted = pytesseract.image_to_string(chinese, lang='chi_sim')
    print(f"------------- 识别中文\r\n {extracted} \r\n-------------")


print(f"Params count: {str(len(sys.argv))}")
print(f"Params: {str(sys.argv)}")
run_times = int(retry)
print(f"Script run times: {run_times}")

while run_times > 0:
    snapshot_and_extract()
    extract_captcha()
    extract_chinese()
    run_times = run_times - 1
