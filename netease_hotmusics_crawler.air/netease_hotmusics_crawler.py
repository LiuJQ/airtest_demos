# -*- encoding=utf8 -*-
__author__ = "Jackin"
__desc__ = """
1. 网易云音乐app-抓取热歌排行榜
2. 录制运行视频、用例跑完后自动生成报告
"""

from airtest.core.android.recorder import *
from airtest.core.android.adb import *
from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__, logdir=r"D:\workspace_python\reports")


def enter_music():
    log("启动云音乐app")
    # 点击同意
    poco("com.netease.cloudmusic:id/agree").wait_for_appearance(timeout=60)
    poco("com.netease.cloudmusic:id/agree").click()

    wait(Template(r"tpl1675330077983.png", record_pos=(-0.001, 0.4), resolution=(1080, 2160)))
    poco("com.android.packageinstaller:id/permission_allow_button").wait_for_appearance(timeout=2)
    poco("com.android.packageinstaller:id/permission_allow_button").click()
    sleep(1.0)

    poco("com.android.packageinstaller:id/permission_allow_button").click()

    # 勾选协议
    poco("com.netease.cloudmusic:id/agreeCheckbox").wait_for_appearance()
    poco("com.netease.cloudmusic:id/agreeCheckbox").click()
    # 点击体验
    poco("com.netease.cloudmusic:id/trialT").click()

    sleep(5.0)

    assert_exists(Template(r"tpl1675330538306.png", record_pos=(0.004, -0.301), resolution=(1080, 2160)),
                  "进入网易云音乐app首页")


def crawling_music():
    # 抓取热歌排行榜
    log("抓取热歌排行榜")
    poco(text="排行榜").click()
    sleep(2.0)

    poco(text="热歌榜").click()
    sleep(2.0)

    assert_exists(Template(r"tpl1675331307927.png", record_pos=(-0.005, -0.669), resolution=(1080, 2160)),
                  "进入热歌榜的歌单")

    # 定义空数组用于存放排行榜的歌名
    titles = []
    # 定义数组目前的长度和最终的长度
    current_count, last_count = len(titles), len(titles)

    while True:
        last_count = len(titles)
        for title in poco("com.netease.cloudmusic:id/musicInfoList").child(
                "com.netease.cloudmusic:id/musicListItemContainer"):
            a = title.offspring("com.netease.cloudmusic:id/songName")
            if not a.exists():
                continue
            name = a.get_text()
            if not name in titles:
                titles.append(name)
                log(f"Fount Music: {name}")

        current_count = len(titles)
        poco.swipe([0.5, 0.7], [0.5, 0.1], duration=2)
        sleep(1.0)

        # 当两者数值相等，即current_count不再增加时，表明爬取完毕
        if current_count == last_count:
            log(f"总共爬取{str(last_count)}首歌曲的名称")
            break


try:
    # 开启录屏
    adb = ADB(serialno="892QAETRHT4XU")
    recorder = Recorder(adb)
    recorder.start_recording()

    # 重启应用，保证初始化状态一致
    clear_app("com.netease.cloudmusic")
    start_app("com.netease.cloudmusic")

    # 初始化Poco
    sleep(5.0)
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    sleep(1.0)

    # 执行用例
    enter_music()
    crawling_music()

    # 结束录屏
    recorder.stop_recording(output=r"D:\workspace_python\reports\netease_hotmusics.mp4")
finally:
    simple_report(__file__, logpath=r"D:\workspace_python\reports", output=r"D:\workspace_python\reports\netease_hotmusics.html")

