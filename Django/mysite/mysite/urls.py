"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from .views import *
from books import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url('^admin/', admin.site.urls),
    path('hello/', hello),
    # path('', my_homepage_view),
    # re_path('^$', my_homepage_view),  # 正则匹配(这个版本似乎不支持)
    url('^$', my_homepage_view),
    path('time/', current_datetime),  # 只能匹配绝对路径，不支持正则
    path('another-time-page/', another_time_page),
    url('^time/plus/(\d{1,2})/$', hours_ahead),  # 支持正则匹配（返回的是re_path的返回值）
    path('another-time-page2', another_time_page_2),
    path('request', display_meta),
    url('^search-form/$', views.search_form),
    url('^search/$', views.search),
    url('^contact-us/$', views.contact),
    url('^TimeCapsule/(\d{4})/(\d{1,2})/(\d{2})/$', time_capsule),
    path('TimeCapsule/MyBirthday/', time_capsule, {'year': 1995,
                                          'month': 7,
                                          'day': 24}),
]

