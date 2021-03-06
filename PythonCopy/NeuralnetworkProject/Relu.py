
# -*- coding:utf-8 -*-
#編集環境ををutf-8にする

#######################################################################################
# ProjectName   : Reluプログラム
# FileName      : Relu.py
# Name          : 木村雅椰
# Year,month,day: 2017,02,21
#
#comment        :
#
#######################################################################################

#######################################################################################
# import
#######################################################################################
import numpy as np  # 高度算術ライブラリ
import sys          # システムパラメータpackage
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
# 関数名 : Relu(x)
# 返り値 : np.maximum(0,x)
# 説明　 : Relu関数
#
#######################################################################################
def Relu(x):
    return np.maximum(0,x)

#######################################################################################
# 関数名 : main()
# 返り値 : なし
# 説明　 : main関数
#
#######################################################################################
def main():
    print(u"Relu関数\n")

    print(u"value : -1")
    print( str( Relu ( -1 ) ) + "\n" )

    print(u"value : 3")
    print( str( Relu ( 3 ) ) + "\n" )

    print("End")
    return 0

#######################################################################################
if __name__ == "__main__":
        sys.exit(main())
