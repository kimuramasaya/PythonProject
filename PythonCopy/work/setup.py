# coding: utf-8
# cx_Freeze 用セットアップファイル

import sys
from cx_Freeze import setup,Executable

####################################################################
# セットアップ
####################################################################

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

exe = Executable(script='html_get.py',
                 base=base)

setup(
    name = 'HtmlImageGeter',
    version = '0.1',
    descriptiom = 'converter',
    executables = [exe]
    )
