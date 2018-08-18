from api_shadowsocks import *
import sys
from daemon import Daemon



configPath = ".\cfg.properties"
if __name__ == '__main__':
    daemon = Daemon(probPoint='google.com', proxy='10.0.0.123:1081')

    

    # ======================================================

    # setShadowSocks可选服务器
    #
    # pattern:所要爬取的服务器的模式.
    # 可选值有(定义在api中):
    # * JapanA_pattern     # 日本服务器A
    # * JapanB_pattern     # 日本服务器B
    # * JapanC_pattern     # 日本服务器C
    # * SingaporeA_pattern # 新加坡服务器A
    # * SingaporeB_pattern # 新加坡服务器B
    # * SingaporeC_pattern # 新加坡服务器C
    # * UsaA_pattern       # 美国服务器A
    # * UsaB_pattern       # 建议不使用
    # * UsaC_pattern       # 建议不使用
    pattern_list = [JapanA_pattern, JapanB_pattern, JapanC_pattern,
                    SingaporeA_pattern, SingaporeB_pattern, SingaporeC_pattern, UsaA_pattern]

    # try:

    # pattern = pattern_list[int(sys.argv[1]) - 1]
    # shadowsocks.setShadowSocks(pattern=None)
    # except IndexError as e:
    # print('[Error]: Lack of index.', e)
