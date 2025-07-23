from django.urls import path

from book.views import create_book, shop, register,json, method, methods

from book.views import set_cookie,get_cookie
from book.views import set_session,get_session

from django.urls import converters

from django.urls.converters import register_converter


class MobileConverter:
    regex = "1[3-9]\d{9}"

    def to_python(self, value):
        return value+'xxxxx'
register_converter(MobileConverter, 'phone')

    # def to_url(self, value):
    #     return value

urlpatterns=[
    path('create/', create_book),
    # path('<city_id>/<shop_id>/', shop),


    path('<int:city_id>/<phone:mobile>/', shop),
    path('register/', register),
    path('json/', json),
    path('method/', method),
    path('res/',methods),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),
]
