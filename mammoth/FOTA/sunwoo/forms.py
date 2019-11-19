from django import forms
from .models import Devicedata, Firmwaredata
# 모델클래스 GuessNumbers로 부터 데이터를 입력 받을 폼을 작성한다.

class PostFormDev(forms.ModelForm):
#forms의 ModelForm 클래스를 상속 받는다.

    class Meta:
        model = Devicedata
        #GuessNumbers와 연결
        fields = ['manufacture', 'deviceName', 'deviceid', 'firmware_version', 'update_date']
        # 해당 모델에서 입력 받을 것들을 정의한다.

class PostFormFirm(forms.ModelForm):
#forms의 ModelForm 클래스를 상속 받는다.

    class Meta:
        model = Firmwaredata
        #GuessNumbers와 연결
        fields = ['manufacture', 'deviceName', 'firmware_version', 'firmware_number', 'file', 'update_date']
        # 해당 모델에서 입력 받을 것들을 정의한다.
