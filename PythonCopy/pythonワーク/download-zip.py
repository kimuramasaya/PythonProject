# -*- coding: utf-8 -*-

#IP�m�FAPI�փA�N�Z�X���Č��ʂ�\������
#���C�u�����̎�荞��
import urllib.request

#�f�[�^���擾����
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

#�o�C�i���𕶎��x�ɕϊ�
text = data.decode("utf-8")
print(text)
