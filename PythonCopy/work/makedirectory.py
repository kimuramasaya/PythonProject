#!/usr/bin/python -S
# -*- coding:utf-8 -*-
#coding: utf-8

#編集環境ををutf-8にする

import os
import sys
import codecs
#os.mkdir('img')#新しくフォルダを作る
#name=os.path.dirname("path")
#print(name)

#ディレクトリーの中身のリストを表示
print(os.path.dirname(os.path.abspath(__file__)))#スクリプトの場所のパス参照
#files = os.listdir(os.path.dirname(os.path.abspath(__file__)))#ディレクトリーの中身のリストを取得
#for file in files:
#    print file

if (os.path.exists("img")):
    print("ExistenceFolder")#すでにフォルダーが存在しています
else:
    print("MakeFolder : img")
    os.mkdir('img')#新しくフォルダを作る


    

        
    
        
        
    
