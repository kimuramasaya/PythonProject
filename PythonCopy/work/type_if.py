
# -*- coding:utf-8 -*-
#編集環境ををutf-8にする

#######################################################################################
# ProjectName   : 型判定プログラム
# FileName      : type_if.py
# Name          : 木村雅椰
# Year,month,day: 2017,02,21
#
#comment        :
#
#######################################################################################

#######################################################################################
# import
#######################################################################################
import sys          #システムパラメータpackage
#######################################################################################

#######################################################################################
# define
#######################################################################################
#MAX_NUMBER = 5
global NUM
NUM = 5,0
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
    print(u"型判定")
    if type(NUM) == int:
        print(u"型一致")
        print(NUM)
    else :
        print(u"型不一致")
        print(int(NUM))#int型にキャストImmutable(不変型)なので型変換できない
        print(u"型判定")
        if type(NUM) == int:
            print(u"キャスト成功")
            print(NUM)
        else:
            print(u"キャスト失敗")
            print(NUM)
    return 0

#######################################################################################
if __name__ == "__main__":
        sys.exit(main())