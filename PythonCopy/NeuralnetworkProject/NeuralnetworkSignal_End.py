
# -*- coding:utf-8 -*-
#編集環境ををutf-8にする

#######################################################################################
# ProjectName   : ニューロラルネットワーク信号伝達プログラム
# FileName      : NeuralnetworkSignal.py
# Name          : 木村雅椰
# Year,month,day: 2017,03,06
#
#comment        :
#
#######################################################################################

#######################################################################################
# import
#######################################################################################
import numpy as np
import time
import SigmoidFunction as F
import NeuralnetworkSignal as Ns
import sys          #システムパラメータpackage
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
# 関数名 : init_network()
# 返り値 : network(辞書オブジェクト)
# 説明　 : networkデータ初期化:値 重み,バイアス
#
#######################################################################################
def Init_network():
    network ={}     #辞書オブジェクト初期化
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['b1'] = np.array([0.1,0.2,0.3])
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2'] = np.array([0.1,0.2])
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['b3'] = np.array([0.1,0.2])

    return network

#######################################################################################
# 関数名 : Forward(network,x)
# 返り値 : y
# 説明　 : networkデータ初期化:値 重み,バイアス
#
#######################################################################################
def Forward(network,x):
    W1,W2,W3 = network['W1'],network['W2'],network['W3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']

    a1 = np.dot(x,W1) + b1
    z1 = F.sigmoid(a1)

    a2 = np.dot(z1,W2) + b2
    z2 = F.sigmoid(a2)

    a3 = np.dot(z2,W3) + b3
    y = Ns.Identity_function(a3)

    return y
#######################################################################################
# 関数名 : main()
# 返り値 : なし
# 説明　 : main関数
#
#######################################################################################
def main():   
    network = Init_network()
    x = np.array([1.0,0.5])
    y = Forward(network,x)
    print(str(y))
    
    time.sleep(10)
    return 0

#######################################################################################
if __name__ == "__main__":
        sys.exit(main())
