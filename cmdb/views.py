from django.shortcuts import render
from cmdb.models import invitation
from django.core.paginator import Paginator # 分页
from django.http import HttpResponseRedirect
# Create your views here.

# 展示、分页
def index(request):
    # 限制每一页显示的条目数量
    limit = 10
    article = invitation.objects
    paginator = Paginator(article,limit)
    # 从url中获取页码参数
    page_num = request.GET.get('page',1)
    loaded = paginator.page(page_num)
    context = {
        'invitation':loaded
    }
    return render(request,"index.html",context)

# 进入添加页面
def toAdd(request):
    return render(request,"add.html")

# 添加
def addInvitation(request):
    if request.method == 'POST':
        number = request.POST.get("number",None)
        title = request.POST.get("title",None)
        content = request.POST.get("content",None)
        url = request.POST.get("url",None)
        tit = "提问：" + str(title) + "  编号：" + str(number)
        # 添加到数据库
        invi = invitation(number = number,title = tit,content = content,url = url)
        invi.save()
    return HttpResponseRedirect('/index/')

# 回显
def toUpdate(request):
    if request.method == 'GET':
        number = request.GET.get("number",None)
    invi = invitation.objects.filter(number=number)
    context = {
        'invitation':invi
    }
    return render(request,"update.html",context)

# 修改
def updateInvitation(request):
    if request.method == 'POST':
        number = request.POST.get("number", None)
        title = request.POST.get("title", None)
        content = request.POST.get("content", None)
        url = request.POST.get("url", None)
        invi = invitation.objects.filter(number=number).update(title=title,content=content,url=url)
    return HttpResponseRedirect('/index/')

# 删除
def delete(requeset):
    if requeset.method == 'GET':
        number = requeset.GET.get("number",None)
    invi = invitation.objects.filter(number=number).delete()
    print(invi)
    return HttpResponseRedirect('/index/')