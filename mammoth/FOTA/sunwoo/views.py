from django.shortcuts import render

# Create your views here.

from .forms import *
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect , get_object_or_404
import urllib
from django.urls import reverse
from django.utils import timezone
# 페이지네이션 구현
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import template

import os
from django.conf import settings
from django.http import HttpResponse, Http404
from io import BytesIO
import zipfile
from django.views.decorators.csrf import csrf_exempt

register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)]


# 로그인
def login(request):
    return render(request, 'sunwoo/index.html', {})

# 계정등록
#def regist_account(request):
#    return render(request, 'sunwoo/regist_account.html', {})

#장치등록
def regist_device(request):
    if request.method=='POST':
        form=PostFormDev(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listdev')
    else:
        form=PostFormDev()
        return render(request, 'sunwoo/regist_device.html', {'form':form})

# 펌웨어 등록
def upload_firmware(request):
    if request.method == "GET":
        form = PostFormFirm()
    if request.method=='POST':
        form=PostFormFirm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form=PostFormFirm()
        return render(request, 'sunwoo/upload_firmware.html', {'form':form})

def del_file(old_file, new_file):
    if old_file != new_file:
        old_file.delete()
    return new_file


###############################################################################################################


def main(request):
    return render(request, 'sunwoo/main.html',{})

def listdev(request):
    Devicedatas = Devicedata.objects.all()
    Firmwaredatas = Firmwaredata.objects.all()
    firmware_checks = list()
    label = False

    for device in Devicedatas:
        label=False
        for firmware in Firmwaredatas:
            if(device.manufacture == firmware.manufacture and device.deviceName == firmware.deviceName and device.firmware_version == firmware.firmware_version):
                firmware_checks.append(True)
                label=True
                break
        if label == False:
            firmware_checks.append(False)


    return render(request, 'sunwoo/listdev.html',{'Devicedatas':Devicedatas, 'firmware_checks': firmware_checks})

def listfirm(request):
    Firmwaredatas=Firmwaredata.objects.all()
    return render(request, 'sunwoo/listfirm.html',{'Firmwaredatas':Firmwaredatas})

def deletedev(request, devkey):
    deldev = Devicedata.objects.get(pk=devkey)
    deldev.delete()
    return redirect('listdev')

def deletefirm(request, firmkey):
    delfirm = Firmwaredata.objects.get(pk=firmkey)
    delfirm.delete()
    return redirect('listfirm')

def editdev(request, id):
    obj=get_object_or_404(Devicedata, id=id)
    if request.method=='POST':
        form=PostFormDev(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('listdev')
    else:
        form=PostFormDev()
        return render(request,'sunwoo/post_form.html',{'form':form})

def editfirm(request, id):
    obj=get_object_or_404(Firmwaredata, id=id)
    old_file = obj.file
    if request.method == "GET":
        form = PostFormFirm()
    if request.method == 'POST':
        form=PostFormFirm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            post = form.save(commit=False)
            new_file = post.file
            post.file = del_file(old_file, new_file)
            post.save()
            return redirect('listfirm')
    else:
        form=PostFormFirm()
        return render(request,'sunwoo/edit_firmware.html',{'form':form})

@csrf_exempt
def download_iphone(request, id, num):
    d_ver = Devicedata.objects.get(deviceid=id)
    firm = Firmwaredata.objects.filter(deviceName=d_ver.deviceName).order_by('-update_date')
    n_ver = firm[0]
    path = 'media/'+str(Firmwaredata.objects.get(deviceName=d_ver.deviceName,firmware_number=num).file)
    response=HttpResponse(open(path,'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=pic_test_'+str(num)+'.png'
    return response

def check_version(request, id):
    d_ver = Devicedata.objects.get(deviceid=id)
    firm = Firmwaredata.objects.filter(deviceName=d_ver.deviceName).order_by('-update_date')
    n_ver = firm[0]
    if d_ver.firmware_version < n_ver.firmware_version: # replace <
        response=HttpResponse("y")
    else:
        response=HttpResponse("n")
    return response


