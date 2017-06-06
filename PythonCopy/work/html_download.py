#-*- coding:utf-8 -*-

import urllib.request

# 画像ファイルのURLを開く
# （urlに画像ファイルのURLを指定）
request = urllib.request.urlopen(url)

# ファイルをバイナリモードで開き、URLの内容を書き込み
# （file_nameに保存時のファイル名を指定）
f = open(file_name, "wb")
f.write(request.read())

# ファイルを閉じる
f.close()
