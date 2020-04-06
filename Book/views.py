from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from Book.models import Book, Author
from Book.models import FIRST_CATEGORY_LIST, TAG_LIST
from utils.mypage import Pagination
from django.db.models import Q
from django.conf import settings


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


def search(request, classification=0, tag=0):
    url_prefix = request.path_info
    # 分页用，获取查询词 为分页做拼接
    qd = request.GET.copy()
    qd._mutable = True
    current_page = request.GET.get('page', 1)
    if classification:
        query_set = Book.objects.filter(first_category=classification).values('id', 'title', 'course_img',
                                                                              'authors__name')
        if request.GET.get('query'):
            q = _get_query_q(request, ['title', 'authors__name', 'isbn', ])  # 按需添加
            query_set = query_set.filter(q)
        page_obj = Pagination(current_page, query_set.count(), url_prefix, qd, per_page)
        data = query_set[page_obj.start:page_obj.end]

        return {'category': category, 'data': data, 'page_html': page_obj.page_html()}

    elif tag:
        query_set = Book.objects.filter(book_tag=tag).values('id', 'title', 'course_img', 'authors__name')
        if request.GET.get('query'):
            q = _get_query_q(request, ['title', 'authors__name', 'isbn', ])  # 按需添加
            query_set = query_set.filter(q)
        page_obj = Pagination(current_page, query_set.count(), url_prefix, qd, per_page)
        data = query_set[page_obj.start:page_obj.end]

        return {'tag': tag, 'data': data, 'page_html': page_obj.page_html()}

    query_set = Book.objects.all().values('id', 'title', 'course_img', 'authors__name')
    q = _get_query_q(request, ['title', 'authors__name', 'isbn', ])  # 按需添加
    query_set = query_set.filter(q)
    page_obj = Pagination(current_page, query_set.count(), url_prefix, qd, per_page)
    data = query_set[page_obj.start:page_obj.end]
    # 区分哪个网址，返回相应网址数据列表
    if url_prefix.split('/')[1] == 'category':
        return {'data': data, 'page_html': page_obj.page_html(), 'category': category,}
    if url_prefix.split('/')[1] == 'tag':
        return {'data': data, 'page_html': page_obj.page_html(), 'tag': tag}


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
        query_set = Book.objects.all()[:3].values('id', 'title', 'course_img', 'authors__name')
        # 2 在页面上展示
        return render(request, 'index.html', {'data': query_set, })


class FirstCategoryView(View):
    def get(self, request, classification=0, tag=0):
        if request.GET.get('query'):
            data = search(request)
            return render(request, 'bookshow_searchshow.html', data)
        data = search(request,classification,tag)
        return render(request, 'bookshow_searchshow.html', data)


# 详情页
class Archives(View):
    def get(self, request, bid):
        if request.GET.get('query'):
            data = search(request)
            return render(request, 'bookshow_searchshow.html', data)
        book_obj = Book.objects.filter(id=int(bid)).first()
        return render(request, 'detail.html', {'book_obj': book_obj, })

