from django.http import HttpResponse

from django.shortcuts import render
from django.views import View

from book.models import BookInfo


# Create your views here.
def create_book(request):
    book = BookInfo.objects.create(
        name='abc',
        pub_date='2000-1-1',
        readcount=10
    )
    return HttpResponse('create')


# def shop(request, city_id, shop_id):
#     #print(city_id, shop_id)
#
#     query_params = request.GET
#     print(query_params)
#     order = query_params.getlist('order')
#
#     print(order)
#     # <QueryDict: {'order': ['readcount']}>
#     return HttpResponse('boom boom boom!!!!!')


def shop(request,city_id, mobile):
    print(city_id,mobile)


    query_prams = request.GET
    print(query_prams)

    order = query_prams.getlist('order')
    print(order)
    return HttpResponse('aaaaaaaaaaa')
def register(request):

    data = request.POST
    print(data)
    return HttpResponse('bbbbbbbbbbb')

def json(request):

    body = request.body
    # print(body)

    body_str= body.decode()
    print(body_str)


    import json
    body_dict=json.loads(body_str)
    print(body_dict)

    print(request.META)
    print(request.META['SERVER_PORT'])
    return HttpResponse('ccccccccccccccc')


def method(request):
    print(request.method)
    return HttpResponse('ddddddddd')

from django.http import HttpResponse, JsonResponse
def methods(request):
    # response = (HttpResponse('123456', status=200))
    # response['name'] = 'itcast'
    info ={
        'mame':'itcast',
        'address':'shunyi'
    }
    response = JsonResponse(data=info)
    return response

def set_cookie(request):

    username=request.GET.get("username")
    password=request.GET.get("password")


    response=HttpResponse('set_cookie')

    response.set_cookie('name',username, max_age=60*60)
    response.set_cookie('pwd',password)
    # response.delete_cookie('name')

    return response
def get_cookie(request):

    print(request.COOKIES)

    name=request.COOKIES.get('name')
    return HttpResponse(name)

def set_session(request):

    username=request.GET.get('username')

    user_id=1
    request.session['user_id']=user_id

    request.session['username']= username

    return HttpResponse("set_session")

def get_session(request):

    user_id=request.session['user_id']
    username=request.session['username']

    content = '{},{}'.format(user_id,username)
    return HttpResponse(content)

from django.contrib.auth.mixins import LoginRequiredMixin

# LoginRequiredMixin 判断用户登录
class OrderView(LoginRequiredMixin,View):

    def get(selfself,request):
        # isLogin=
        # if not isLogin:
        #     return HttpResponse('你没有登录，页面跳转中～～～～')
        return HttpResponse('get我的订单界面，这个界面必须登录')

    def post(self,request):

        return HttpResponse('post 我的订单，这个界面必须要登录')



def test_view(request):
    return HttpResponse("强制触发响应")