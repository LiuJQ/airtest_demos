# -*- encoding=utf8 -*-
__author__ = "Jackin"

from airtest.core.api import *
auto_setup(__file__)

# 设置全局图片精度为75
ST.SNAPSHOT_QUALITY = 75


def login():
    log("开始登录操作")

    # 利用包名打开LinkFox
    start_app("com.zixun.linkfox")
    sleep(2)

    # 点击“我的”
    touch(Template(r"tpl1675317189645.png", record_pos=(0.374, 0.906), resolution=(1080, 2160)))
    sleep(1)

    # 点击“立即登录”
    touch(Template(r"tpl1675317479495.png", record_pos=(-0.336, -0.708), resolution=(1080, 2160)))
    sleep(1)

    # 点击账号输入框
    touch(Template(r"tpl1675317460880.png", record_pos=(-0.251, -0.199), resolution=(1080, 2160)))
    sleep(1)

    # 输入账号
    log("输入账号")
    text("13387654321")
    sleep(1)

    # 点击登录按钮
    touch(Template(r"tpl1675317551128.png", record_pos=(-0.006, 0.079), resolution=(1080, 2160)))
    sleep(1)

    # 输入预设验证码
    log("输入验证码")
    text("753869")
    sleep(2)


def ensure_login():
    log("以下步骤完成登录操作")
    try:
        login()
    finally:
        assert_exists(Template(r"tpl1675317690483.png", record_pos=(0.373, 0.919), resolution=(1080, 2160)), "登录成功")


# ensure_login()
