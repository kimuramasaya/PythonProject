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
# 関数名 : ChangeDirectory()
# 返り値 : None
# 説明　 : 現在のディレクトリから対象のディレクトリに変更する
#
#######################################################################################
def ChangeDirectory ():
    if (os.path.exists("img")):
        os.chdir("./img")
        print(u"Console : 現在の作業ディレクトリ : "+os.getcwd())

#######################################################################################
# 関数名 : MakeDirectoryNameExists(resource)
# 返り値 : None
# 説明　 : 現在のディレクトリに指定名のフォルダを作る
#
#######################################################################################
def MakeDirectoryNameExists (name):
    print(u"Console : フォルダーを作成します : "+name)
    if (os.path.exists(name)):
        print(u"Console : すでにフォルダーが存在しています")#すでにフォルダーが存在しています
    else:
        print(u"Console : 新しくフォルダを作成します : "+name)
        os.mkdir(name)#新しくフォルダを作る    

#######################################################################################
# 関数名 : download(resource)
# 返り値 : 失敗したURLのリスト
# 説明　 : url情報からhtmlrequestを送りダウンロードする
#
#######################################################################################
def Download(resource):

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

#######################################################################################
# 関数名 : htmlrequest(url)
# 返り値 : html
# 説明　 : url情報からhtmlrequestを送りhtml情報を返す
#
#######################################################################################
def HtmlRequest(url):
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

#######################################################################################
# 関数名 : decode(html)
# 返り値 : html
# 説明　 : Html情報からエンコードデータをデコードしてhtml情報を返す
#
#######################################################################################
def Decode(html):
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

#######################################################################################
# 関数名 : gettagscraping(html)
# 返り値 : soup(BeautifulSoupオブジェクト)
# 説明　 : htmlデータから<a>タグと<href>タグを抽出対象のURL情報を取り出す
#
#######################################################################################
def GetTagScraping(html):

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
        url_str = Download(resource)
        if url_str != None :
            Failure_List.append(url_str)
        
    print(u"Console : 失敗したリスト")
    for Failure in Failure_List:
        print(Failure)
        print(" ")

    print(u"Console : タグの抽出が完了しました")

    #10秒待機
    time.sleep(10)

    #コンソール描画消去
#    os.system("cls")
    
    return soup

#######################################################################################
# 関数名 : main()
# 返り値 : なし
# 説明　 : main関数ここで走らせる
#
#######################################################################################
def main():
    print(u"Console : プログラムを起動")

    #新しい名前のディレクトリを作る
    MakeDirectoryNameExists("img")

    #指定ディレクトリに変更
    ChangeDirectory()

    print(u"Console : 対象URLを入力してください")
    url = raw_input()
    #URL値を入れる
    #url = "http://lovelivepress.com/"

    print("Console : "+url)

    html = HtmlRequest(url)
    if html==None:
        print(u"Console : エラー : htmlrequest")
        return -1

    html = Decode(html)

    GetTagScraping(html)

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
