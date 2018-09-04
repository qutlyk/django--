from django.http import HttpResponse
from django.shortcuts import render
from codestudy.models import Student
from codestudy.models import Root
from django.contrib.auth.decorators import login_required
from django.db import transaction
import time
from django.http import HttpResponseRedirect, HttpResponse

def index(request):     #返回登陆页面
    return render (request, 'func.html')



def get_time():   #获取系统时间
    times = time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime (time.time ()))
    return times


def edit(request):  #进入修改页面
    if request.method == 'GET':
        return render (request, 'index.html')   #如果是get方式 则返回到登陆页面
    if request.method == 'POST':
        no = request.POST.get('edit_name')    #若为post 获取要修改的学号
        obj = Student.objects.filter(no = no)
        if obj:
            return  render(request,'edit_user.html',{'obj':obj})  #将要修改的信息传递到修改页面
        else:
            return render(request,'NotFound.html')


def edit_message(request):  #修改信息 数据交互
    if request.method == 'POST':
        no = request.POST.get('edit_no')
        name = request.POST.get('edit_name')
        age = request.POST.get ('edit_age')
        chinese = request.POST.get ('edit_chinese')
        math = request.POST.get ('edit_math')
        english = request.POST.get ('edit_english')
        sport = request.POST.get ('edit_sport')
        Student.objects.filter(no = no).update(no = no,name = name,age = age,chinese = chinese,math = math,
                     english = english,sport = sport)  #更新语句
        all = Student.objects.all()     #将更新后的信息传到前端
        return  render(request,'show.html',{'show':all})
    else:
        return render (request, 'index.html')

def search(request):  #按学号搜索
    if request.method == 'POST':   #判断是否为post
        result = request.POST.get('search')    #获取输入的值
        show = Student.objects.filter(no = result)   #过滤 获取符合条件下的值
        if show:
            return render(request,'show.html',{'show':show})  #传递回前端
        else:
            return render(request,'NotFound.html')
    else:
        return render (request, 'index.html')  #如果为其他方式，则返回登陆页面


def sort_math(request):   #按数学成绩降序
    re = Student.objects.all().order_by('-math')  #排序
    return render(request,'sort_math.html',{'re':re})


def sort_chinese(request):   #按语文成绩降序
    re = Student.objects.all().order_by('-chinese')  #排序
    return render(request,'sort_math.html',{'re':re})

def sort_english(request):   #按英语成绩降序
    re = Student.objects.all().order_by('-english')  #排序
    return render(request,'sort_math.html',{'re':re})

def sort_sport(request):   #按体育成绩降序
    re = Student.objects.all().order_by('-sport')  #排序
    return render(request,'sort_math.html',{'re':re})


def del_user(request): #删除信息
    if request.method == "POST":
        no = request.POST.get('del_id')
        Student.objects.filter(no = no).delete()
        print('删除成功')
        return render(request,"show.html",{'show':Student.objects.all()})
    else:
        return render(request,"show.html")

def add(request):  #添加
    return render(request,'add.html')  #跳转到添加信息页面

def add_message(request):  #添加信息
    if request.method == "POST":        #判断是否为post提交方式
        no = request.POST.get('add_no',None)
        name = request.POST.get('add_name',None)
        age = request.POST.get('add_age',None)
        chinese = request.POST.get('add_chinese',None)
        math = request.POST.get ('add_math', None)
        english = request.POST.get ('add_english', None)
        sport = request.POST.get ('add_sport', None)  #获取输入的信息 前后台数据交互
        re = Student.objects.filter(no = no)    #判断学号是否存在  filter
        message = ""
        if re:
            message = "学号已存在"
            return render (request, 'add.html',{'message':message})
        try:
            with transaction.atomic ():
                result = Student(no = no,name = name,age = age,chinese = chinese,math = math,english = english
                                 ,sport = sport)  #若不存在，则将信息写入数据库保存
                if result:
                    result.save()
                    print('添加成功')
                    show = Student.objects.all()
                    return render(request,'show.html',{'show':show})  #跳转到显示信息页面
                else:
                    print('添加失败，事务回滚')
        except Exception as e:
            return render(request,"NotFound.html")
    else:
        return render(request,"index.html")

def func(request):
    if request.method == 'GET':
        return render(request,'index.html')
    show = Student.objects.all ()
    if show:
        return render (request, 'show.html',{'show':show})
    else:
        print('数据为空')


def admin_login(request):   #管理员登陆判断
    if request.method == 'POST':
        name = request.POST.get('root')
        passwd = request.POST.get('passwd')
        if name and passwd:     #验证账号密码是否正确
            result = Root.objects.filter(name = name,passwd = passwd)
            if result:
                print('登陆成功')
                show = Student.objects.all()        #登陆成功后显示后台管理页面
                if show:
                    print(name)
                    return  render(request,'show.html',{'show':show,"name":name})
            else:
                print('登陆失败')
        else:
            print('用户不存在')
    else:
        return render(request,'index.html')
