"""Ebook_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Book import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 首页
    url(r'^index/', views.IndexView.as_view(), name='index'),
    # 分类
    url(r'^category/$', views.FirstCategoryView.as_view(), name='category'),
    url(r'^category/(?P<classification>\d+)/$', views.FirstCategoryView.as_view(), name='classification'),
    # 标签
    url(r'^tag/$', views.TagView.as_view(), name='tag'),
    url(r'^tag/(?P<ntag>\d+)/$', views.TagView.as_view(), name='ntag'),
    # 详情页
    # 可能存在的问题是用的数据库id做bid，容易暴露，可换成自己的编号，后期可添加到表中
    url(r'^archives/$', views.Archives.as_view(),name='qarchives'),
    url(r'^archives/(?P<bid>\d+)/$', views.Archives.as_view(),name='archives'),
    url(r'^archives/(?P<bid>\d+)/download/$', views.Download.as_view(),name='download'),
    # 除以上均跳转到首页
    # url(r'^.*/$', views.IndexView.as_view()),
    url(r'^$', views.IndexView.as_view()),
]
