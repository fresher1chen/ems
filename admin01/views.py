import time

from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render,redirect,HttpResponse
from admin01.models import EmpList
import uuid,os
# Create your views here.
#
def addemp(request):
    return render(request, 'adminapp/addEmp.html')

def addlogic(request):
    try:
        with transaction.atomic():
            name = request.POST.get('name')
            salary = request.POST.get('salary')
            age = request.POST.get('age')
            headpic = request.FILES.get('headpic')
            headpic.name = generateUUID(headpic.name)  #避免上传的文件重名，改变名字
            result = EmpList.objects.create(name=name,salary=salary,age=age,headpic=headpic)
            EmpList.objects.update()
            if result:
                return redirect('admin01:emplist')
            return HttpResponse('添加失败')
    except:
        print('error')
        return redirect('admin01:addemp')




def emplist(request):
    number = request.GET.get('page')
    if not number :
        number = 1
    # print(number)
    empli = EmpList.objects.all()
    pagtor = Paginator(empli,per_page=2)
    # print(pagtor.count)
    page = pagtor.page(number)
    return render(request, 'adminapp/emplist.html',{
        'page': page,
})



def updateemp(request):
    try:
        id1=request.GET.get('id')
        return render(request, 'adminapp/updateEmp.html',{
            'upemp':EmpList.objects.get(id=id1)
        })
    except:
        render(request,'adminapp/updateEmp.html')


def updatelogic(request):
    try:
        with transaction.atomic():
            id1 = request.POST.get('id')
            name = request.POST.get('name')
            salary = request.POST.get('salary')
            age = request.POST.get('age')
            u = EmpList.objects.get(id=id1)
            u.name = name
            u.salary=salary
            u.age=age
            u.save()
            # aa=EmpList.objects.all()
            # print(aa)
            return redirect('admin01:emplist')
    except:
        print('error')

# def delete(request,id):
def delete(request):
    try:
        with transaction.atomic():
            id1 = request.GET.get('id')
            # print(id1)
            a = EmpList.objects.get(id=id1)
            a.delete()
            return redirect('admin01:emplist')
    except:
        print('重试')


def generateUUID(filedname):
    id = str(uuid.uuid4())  #生成一个伪随机数，
    extend = os.path.splitext(filedname)[1] #将传进去的文件名进行分割，分成文件名与扩展名，此处取拓展名

    return id+extend