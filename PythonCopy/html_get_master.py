# -*- coding:utf-8 -*-
#編集環境ををutf-8にする

#######################################################################################
# ProjectName   : Webクローラープログラム
# FileName      : html_get.py
# Name          : 木村雅椰
# Year,month,day: 2017,02,08
#
#comment        : 作るにあたってHTMLリクエストを送りすぎないように待機時間を必ず3秒以上
# 設ける設けなかった場合Dos攻撃にあたり法的手段を取られる可能性があるので厳重に注意
# Robot.txtを参照すべし,著作権も考慮して情報取得と公開を判断してね。
#
#######################################################################################

#######################################################################################
# import
#######################################################################################
import os                    # os (ファイル操作用)
import sys                   # sys(システム操作)
from six.moves import urllib # six , urllibc (Python3,Python2互換性ユーティリティでurllibをimport)
import time                  # time (時間処理用)
import bs4                   # BeautifulSoup4 (スクレイピング用)
import chardet               # chardet(Python3 , Python3互換性あり:文字コード解析用)
from tqdm import tqdm        # 進捗バーライブラリー
#######################################################################################

#######################################################################################
# 関数名 : TextLoad (text)
# 返り値 : なし
# 説明　 : main関数ここで走らせる
#
#######################################################################################
def TextLoad (text):
    print(text)
    f = open(text)
    lines2 = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()
    # lines2: リスト。要素は1行の文字列データ
 
    return lines2

def TextExpt (List):
    
    f = open('\Python27\ErrorList.txt', 'w')
    for ListCnt in List:
        f.write(str(ListCnt) + "\n")
    f.close()
    

#######################################################################################
# class
#######################################################################################
#スクレイプクラス
class CScrap :
    m_url = None
    
    def __init__(self):
        m_url = ""

    def ChangeDirectory (self):
        if (os.path.exists("img")):
            os.chdir("./img")
            print(u"Console : 現在の作業ディレクトリ : "+os.getcwd())

    def MakeDirectoryNameExists (self,name):
        print(u"Console : フォルダーを作成します : "+name)
        if (os.path.exists(name)):
            print(u"Console : すでにフォルダーが存在しています")#すでにフォルダーが存在しています
        else:
            print(u"Console : 新しくフォルダを作成します : "+name)#フォルダが存在していない場合
            os.mkdir(name)#新しくフォルダを作る    

    def Download(self,resource):
        Failure = None
        print(u"Console : ダウンロード : "+resource)
        #1.5秒待機
        time.sleep(1.5)
        #引数(url)からファイルを開く
        request = urllib.request.urlopen(resource)
        if request.code != 200:
            print("Console : code 200")
        os.system("cls")
        #ファイルをバイナリモードで開き内容を書き込み
        try :
            with open(os.path.basename(resource), "wb" ) as f:#code 22ですり抜けさせる
                f.write( request.read() )
                print(u"Console : 保存しました")
        except IOError:
            Failure = resource
            print(u"Console : 保存できません")
        else :
            #ファイルを閉じる
            f.close()
            request.close()
        return Failure

    def HtmlRequest(self,url):
        print(u"Console : HTMLリクエスト")
        # 1START HTML取得
        #5秒待機
        time.sleep(5)
        #HTML取得命令
        try :
            request = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e: #HTTPエラー
            print(e.code)
            return None
        except urllib.error.URLError as e: #URLエラー
            print(e.reason)
            return None
        #5秒待機
        time.sleep(5)
        #HTML読み込み
        html = request.read()
        #内容表示
        print(html)
        print(u"Console : HTMLを取得しました")
        #10秒待機
        time.sleep(10)
        #コンソール描画消去
        os.system("cls")
        return html
    
    def Decode(self,html):
        print(u"Console : デコードを開始します")
        html.decode(chardet.detect(html)['encoding'].lower())
        print(html.decode(chardet.detect(html)['encoding'].lower()))
        #10秒待機
        time.sleep(5)
        #文字コードを返す(success)
        print(u"Console : "+chardet.detect(html)['encoding'].lower()+u"でデコードしました")
        #5秒待機
        time.sleep(5)
        print(u"Console : デコードを終了します")
        #10秒待機
        time.sleep(10)
        #コンソール描画消去
        os.system("cls")
        return html

    def GetTagScraping(self,html):
        print(u"Console : HTMLから<img>タグと<src>タグを抽出します")
        resources = []
        Failure_List = []
        # BeautifulSoupオブジェクトを作成
        soup = bs4.BeautifulSoup(html)
        # htmlのすべてのaタグの中のhref属性の内容を取得(ここ改良すべき)取り方が辺
        for a_tag in tqdm(soup.find_all("img")):    #<img>タグすべて追加
            href_str = a_tag.get("src")    #<src>タグの内容を値取得して追加
            resources.append(href_str)      #リストオブジェクトに追加

        for resource in tqdm(resources):
            print(resource)
            url_str = self.Download(resource)
            if url_str != None :
                Failure_List.append(url_str)
        print(u"Console : 失敗したリスト")
        for Failure in Failure_List:
            print(Failure)
            print(" ")

        TextExpt(Failure_List)

        
        print(u"Console : タグの抽出が完了しました")
        #10秒待機
        time.sleep(10)

        return soup

    def SetUrl (self , url):
        m_url = url
        
#######################################################################################
        
#######################################################################################
# 関数名 : main()
# 返り値 : なし
# 説明　 : main関数ここで走らせる
#
#######################################################################################
def main():

    print(u"Console : プログラムを起動")

    #クラスオブジェクトをコンストラクターに通す
    C_Object = CScrap()

    #新しい名前のディレクトリを作る
    C_Object.MakeDirectoryNameExists("img")

    #指定ディレクトリに変更
    C_Object.ChangeDirectory()

    print(u"Console : 対象URLを入力してください")

    #C_Object.SetUrl(raw_input())

    
    line = TextLoad('\Python27\UrlList.txt')
    for linecnt in line:
        url = linecnt
        #URL値を入れる
        #url = "http://lovelivepress.com/"

        #print("Console : "+C_Object.m_url)

        html = C_Object.HtmlRequest(url)
        if html==None:
            print(u"Console : エラー : htmlrequest")
            return -1

        html = C_Object.Decode(html)

        C_Object.GetTagScraping(html)

        #5秒待機
        time.sleep(5)
    
    
    print(u"Console : 全てのタスクが終了しました")
    print(u"Console : 10秒後にプログラムを終了します")

    #10秒待機
    time.sleep(10)
    
    return 0

#######################################################################################
if __name__ == "__main__":
        sys.exit(main())
