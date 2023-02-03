# -*- encoding=utf8 -*-
__author__ = "Jackin"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__, devices=["Android://127.0.0.1:5037/892QAETRHT4XU"])

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

package_name = 'com.ss.android.ugc.aweme'
activity_name = 'splash.SplashActivity'

start_app(package_name, activity=activity_name)

device_attrs = device()
print(device_attrs.uuid)

width, height = device_attrs.get_current_resolution()
print('width={}, height={}'.format(width, height))

# 开始刷抖音
while True:
    # 滑动一次
    swipe((width * 0.5, height * 3 / 4), (width * 0.5, height / 4), duration=0.1)
    sleep(5)

poco().swipe(direction='up')
