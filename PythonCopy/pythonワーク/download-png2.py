# -*- coding: utf-8 -*-

#���C�u�����̎�荞��
import urllib.request

#URL�ƕۑ��p�X���w��
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

#�_�E�����[�h
mem = urllib.request.urlopen(url).read()

#�t�@�C���֕ۑ�
with open(savename ,mode = "wb") as f :
    f.write(mem)
    print(u"�ۑ����܂���")
