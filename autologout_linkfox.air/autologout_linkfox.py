# -*- encoding=utf8 -*-
__author__ = "Jackin"

from airtest.core.api import *
import sys
sys.path.append("D:/workspace_python/python_study/autologin_linkfox.air")

auto_setup(__file__)

using("autologin_linkfox.air")
from autologin_linkfox import login

# 设置全局图片精度为75
ST.SNAPSHOT_QUALITY = 75


def assert_login():
    log("以下步骤确保当前已登录")

    # 判断当前是否已登录
    login_or_not = exists(
        Template(r"tpl1675318920299.png", threshold=0.9, record_pos=(0.374, 0.919), resolution=(1080, 2160)))
    log(f"login status: {login_or_not}")
    if not login_or_not:
        login()
        sleep(2)


def logout():
    log("以下步骤开始退出登录")

    # 进入用户中心
    touch(Template(r"tpl1675321499138.png", threshold=0.9, record_pos=(-0.15, -0.664), resolution=(1080, 2160)))

    sleep(0.5)

    # 点击退出登录
    touch(Template(r"tpl1675321207034.png", record_pos=(-0.003, 0.804), resolution=(1080, 2160)))

    # 确认退出登录
    if exists(Template(r"tpl1675321239600.png", record_pos=(-0.012, 0.61), resolution=(1080, 2160))):
        touch(Template(r"tpl1675321256096.png", record_pos=(0.198, 0.805), resolution=(1080, 2160)))

    sleep(1)


try:
    # 利用包名打开LinkFox
    start_app("com.zixun.linkfox")
    sleep(2)

    # 确保已登录
    assert_login()

    # 退出登录
    logout()
finally:
    assert_exists(Template(r"tpl1675321316165.png", record_pos=(-0.11, -0.738), resolution=(1080, 2160)), "退出登录")

    log("已完成登出操作")
