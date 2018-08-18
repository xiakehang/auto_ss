
# -*- coding: utf-8 -*-
# @Author   :
# @DateTime :
import os
import sys
import re
import subprocess
import time
import threading

from api_shadowsocks import *

# 更改为你的ss程序路径
ssPath = ".\Shadowsocks\Shadowsocks.exe"  # 当前是相对路径

# 更换为你的ss配置文件路径
ssConfigPath = ".\Shadowsocks\gui-config.json"  # 当前是相对路径


class Daemon(object):

    def __init__(self, probPoint='google.com', proxy='10.0.0.123:1081'):

        super(Daemon, self).__init__()

        self.probPoint = probPoint
        self.proxyServer = proxy.split(':')[0]
        self.proxyPort = proxy.split(':')[1]

        self.proxyGood = False

        self.failures = 0

        shadowsocks = ShadowSocks(ssPath=ssPath, ssConfigPath=ssConfigPath)
        shadowsocks.setShadowSocks(pattern=None)

        threading.Thread(target=self.startTest, args=None).start()
        threading.Thread(target=self.watch, args=None).start()

        self.startTest()

    def startTest(self):
        while self.failures < 10:
            self.test()
            time.sleep(20)

    def watch(self):
        while True:
            if (self.proxyGood != True):
                if (self.failures > 2 and self.failures < 10):
                    shadowsocks = ShadowSocks(
                        ssPath=ssPath, ssConfigPath=ssConfigPath)
                    shadowsocks.setShadowSocks(pattern=None)
                else:
                    print('connection lost... please check your network ')

            time.sleep(10)

    def test(self):
        rslt = self.check()
        if (rslt == False):
            self.failures += 1
            self.proxyGood = False

        if (rslt == True):
            self.failures = 0
            self.proxyGood = True

    def check(self):
        try:
            # exec wget to check internet connectoin, and dump result into a txt file
            cmds = [
                'set https_proxy=http://10.0.0.123:1081',
                'wget -O check.png --timeout 2 --tries 2 --output-file check.txt https://www.google.com/textinputassistant/tia.png'
            ]

            print('checking internet connection...')
            p = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='GB2312')
            for cmd in cmds:
                r = p.stdin.write(cmd + "\n")

            p.stdin.close()

            # read check.txt
            out = ''
            with open('./check.txt') as f:
                for line in f.readlines():
                    out += line

            print(out)

            regex = re.compile('100%')

            # print(out)
            if len(regex.findall(out)) != 0:
                print('ss connecton is good')
                return True

            else:
                print('ss connecton is down, failures: ' + str(self.failures + 1))
                return False

        except Exception as e:
            print('Network connection checking error!')
            return 'ERR'
