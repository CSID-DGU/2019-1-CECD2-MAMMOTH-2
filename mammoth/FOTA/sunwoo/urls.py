from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^$', views.login, name='login'),
                url(r'^registDevice/$', views.regist_device, name='registDevice'),
                url(r'^uploadFirmware/$', views.upload_firmware, name='uploadFirmware'),
                url(r'^main/$', views.main, name='main'),
                url(r'^listdev/$', views.listdev, name='listdev'),
                url(r'^listfirm/$', views.listfirm, name='listfirm'),
                url(r'^deletedev/(?P<devkey>[0-9]+)/$', views.deletedev, name='deletedev'),
                url(r'^deletefirm/(?P<firmkey>[0-9]+)/$', views.deletefirm, name='deletefirm'),
                url(r'^editdev/(?P<id>[0-9]+)/$', views.editdev, name='editdev'),
                url(r'^editfirm/(?P<id>[0-9]+)/$', views.editfirm, name='editfirm'),
                #url(r'^download/iphone/(?P<d_version>[0-9]+)/$', views.download_iphone, name='download_iphone'),
                url(r'^download/iphone/(?P<id>[0-9]+)/(?P<num>[0-9]+)/$', views.download_iphone, name='download_iphone'),
                url(r'check_version/(?P<id>[0-9]+)/$', views.check_version, name='check_version'),
                ]
