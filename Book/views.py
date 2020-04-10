from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from Book.models import Book, Author, AccessCode, Tag
from Book.models import FIRST_CATEGORY_LIST, TAG_LIST
from utils.mypage import Pagination
from django.db.models import Q
from django.conf import settings
import logging
from django.http import JsonResponse

# 缓存使用redis时使用
# from django_redis import get_redis_connection
# conn = get_redis_connection("default")

# 生成一个以当前模块名为名字的logger实例
logger = logging.getLogger(__name__)
# collect_logger = logging.getLogger('collect')


per_page = settings.PER_PAGE

# Create your views here.
category = []
for i in range(len(FIRST_CATEGORY_LIST)):
    category.append(FIRST_CATEGORY_LIST[i])

tag_list = []
for i in range(len(TAG_LIST)):
    tag_list.append(TAG_LIST[i])


def _get_query_q(request, field_list, op='OR'):
    query_value = request.GET.get('query', '')
    q = Q()
    q.connector = op

    for field in field_list:
        q.children.append(Q(('{}__icontains'.format(field), query_value)))
    return q


def search(request, classification=0, ntag=0):
    url_prefix = request.path_info
    # 分页用，获取查询词 为分页做拼接
    qd = request.GET.copy()
    qd._mutable = True
    current_page = request.GET.get('page', 1)
    if classification:
        query_set = Book.objects.filter(first_category=classification)

    elif ntag:
        tag = Tag.objects.filter(id=ntag)
        query_set = Book.objects.filter(tags=tag)
    else:
        query_set = Book.objects.all()
        # print(query_set)

    # q = _get_query_q(request, ['title', 'authors__name', 'isbn', ])  # 模糊检索字段，按需添加
    # query_set = query_set.filter(q)
    # page_obj = Pagination(current_page, query_set.count(), url_prefix, qd, per_page)
    # data = query_set[page_obj.start:page_obj.end]
    # 区分是否为搜索
    if request.GET.get('query'):
        q = _get_query_q(request, ['title', 'authors__name', 'isbn','tags__name'])  # 模糊检索字段，按需添加
        query_set = query_set.filter(q)
        query_set = query_set.distinct()
        page_obj = Pagination(current_page, query_set.count(), url_prefix, qd, per_page)
        data = query_set[page_obj.start:page_obj.end]
        return {'data': data, 'page_html': page_obj.page_html()}
    # 不是搜索请求， 区分哪个网址，返回相应网址数据列表

    page_obj = Pagination(current_page, query_set.count(), url_prefix, qd, per_page)
    data = query_set[page_obj.start:page_obj.end]
    if url_prefix.split('/')[1] == 'category':
        if url_prefix.split('/')[2]:
            return {'data': data, 'page_html': page_obj.page_html(), 'category': category,
                'categorynum': int(url_prefix.split('/')[2])}
        return {'data': data, 'page_html': page_obj.page_html(), 'category': category, }
    elif url_prefix.split('/')[1] == 'tag':
        if url_prefix.split('/')[2]:
            return {'data': data, 'page_html': page_obj.page_html(), 'tag': tag_list,
                'tagnum': int(url_prefix.split('/')[2])}
        return {'data': data, 'page_html': page_obj.page_html(), 'tag': tag_list, }
    return {'data': data, 'page_html': page_obj.page_html(), }


# 首页
class IndexView(View):
    def get(self, request):
        # 展示首页页面-网站的信息、分类、搜索框、展示多少热门图书，标签
        # 需要数据：图书表的信息
        # 额外功能：分页 搜索
        # 默认展示10条热门图书
        # 1 获取所有的相关图书信息
        if request.GET.get('query'):
            data = search(request)
            return render(request, 'bookshow_searchshow.html', data)
        query_set = Book.objects.all()[:3]
        # 2 在页面上展示
        return render(request, 'index.html', {'data': query_set, })


# 分类
class FirstCategoryView(View):
    def get(self, request, classification=0):
        if request.GET.get('query'):
            data = search(request)
            return render(request, 'bookshow_searchshow.html', data)
        data = search(request, classification=classification)
        return render(request, 'bookshow_searchshow.html', data)


# 标签
class TagView(View):
    def get(self, request, ntag=0):
        if request.GET.get('query'):
            data = search(request)
            return render(request, 'bookshow_searchshow.html', data)
        data = search(request, ntag=ntag)
        return render(request, 'bookshow_searchshow.html', data)


# 详情页
class Archives(View):
    def get(self, request, bid=0):
        if request.GET.get('query'):
            data = search(request)
            return render(request, 'bookshow_searchshow.html', data)
        if bid == 0:
            return redirect('/index')
        book_obj = Book.objects.filter(id=int(bid))
        return render(request, 'detail.html', {'book_obj': book_obj, })


class Download(View):
    def get(self, request, bid=0):
        if request.GET.get('query'):
            data = search(request)
            return render(request, 'bookshow_searchshow.html', data)
        if bid == 0:
            return redirect('/index')
        book_obj = Book.objects.filter(id=int(bid)).first()
        return render(request, 'download.html', {'book_obj': book_obj, })


    def post(self, request, bid):
        book_obj = Book.objects.filter(id=int(bid)).first()
        # 设置状态码，前端页面做页面判断
        res = {"code": "0"}
        # 获取数据库中设置的验证码
        access_code = AccessCode.objects.all().values('access_code')
        access_code_list = []
        for i in access_code:
            access_code_list.append(i['access_code'])
        # 获取用户输入
        accessCode = request.POST.get('accessCode')
        # 判断输入是否正确
        if accessCode in access_code_list:
            res["code"] = '1'
        return render(request, 'download.html', {'res': res, 'book_obj': book_obj})

