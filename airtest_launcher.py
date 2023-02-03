# -*- encoding=utf8 -*-
__author__ = "Jackin"

from airtest.cli.runner import AirtestCase, run_script
from airtest.cli.parser import runner_parser


class CustomAirtestCase(AirtestCase):
    def setUp(self):
        # 在air脚本运行之前获取这个自定义的参数
        if self.args.retry:
            self.scope['retry'] = self.args.retry


if __name__ == '__main__':
    ap = runner_parser()
    # 添加自定义的命令行参数
    ap.add_argument("--retry", help="The number of times the script will be run")
    args = ap.parse_args()
    run_script(args, CustomAirtestCase)

# 启动器运行方式
# python .\airtest_launcher.py .\airtest_ocr.air --device android://127.0.0.1:5037/892QAETRHT4XU --retry 3
