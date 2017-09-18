from django.shortcuts import render, redirect
from .models import Item
from redis import Redis
import time
import hashlib
from django.http import HttpResponse

redis = Redis(host='redis', port=6379)


def home(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    counter = redis.incr('counter')
    return render(request, 'home.html', {'items': items, 'counter': counter})

def gzh_access(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    if request.method == 'GET':
        #下面这四个参数是在接入时，微信的服务器发送过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        print("***********" + echostr)
        #这个token是我们自己来定义的，并且这个要填写在开发文档中的Token的位置
        token = 'kuaishoudownloadswwww'

        #把token，timestamp, nonce放在一个序列中，并且按字符排序
        hashlist = [token, timestamp, nonce]
        hashlist.sort()

        #将上面的序列合成一个字符串
        hashstr = ''.join([s for s in hashlist])

        #通过python标准库中的sha1加密算法，处理上面的字符串，形成新的字符串。
        hashstr = hashlib.sha1(hashstr.encode('utf-8')).hexdigest()
        #把我们生成的字符串和微信服务器发送过来的字符串比较，
        #如果相同，就把服务器发过来的echostr字符串返回去
        if hashstr == signature:
            return HttpResponse(echostr)

    items = Item.objects.all()
    counter = redis.incr('counter')
    return render(request, 'home.html', {'items': items, 'counter': counter})
