# -*- coding: utf-8 -*-

#���C�u�����̎�荞��
import urllib.request

#URL�ƕۑ��p�X���w��
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

#�_�E�����[�h
urllib.request.urlretrieve(url,savename)
print(u"�ۑ����܂���")
