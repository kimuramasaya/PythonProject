
# -*- coding:utf-8 -*-
#編集環境ををutf-8にする

#######################################################################################
# ProjectName   : マルチキャストUDP受信プログラム
# FileName      : UdpRecvMultcast.py
# Name          : 木村雅椰
# Year,month,day: 2017,02,23
#
#comment        :
#
#######################################################################################

#######################################################################################
# import
#######################################################################################
from __future__ import print_function
import socket                            #通信
from contextlib import closing   
import sys                               #システムパラメータpackage
#######################################################################################

#######################################################################################
# define
#######################################################################################
#MAX_NUMBER = 5
#######################################################################################

#######################################################################################
# Class
#######################################################################################

#######################################################################################
# GlobalVariable
#######################################################################################


#######################################################################################
# 関数名 : main()
# 返り値 : なし
# 説明　 : main関数
#
#######################################################################################
def main():

    local_address = '172.29.25.130'   # 送信側のPCのIPアドレス
    multicast_group = '239.255.0.1' # マルチキャストアドレス
    port = 4000
    bufsize = 4096
    
    with closing(socket.socket(socket.AF_INET,socket.SOCK_DGRAM)) as sock :
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock.bind(('',port))
        sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,socket.inet_aton(multicast_group)+socket.inet_aton(local_address))

        
        while True:
            print(sock.recv(bufsize))
    
    return 0

#######################################################################################
if __name__ == "__main__":
        sys.exit(main())