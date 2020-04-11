from django.test import TestCase

# Create your tests here.

# str1 = '古典 投资 短篇 文化 政治 大家小书 心理学 旅行 恋爱 书单 三毛 学习 中篇 经典 长篇 诗词 创业 阅读 文艺 散文 哲学 下载 外国文学 人物 日本 心灵 励志 生活 合集 中国 必读 随笔 社会 英国 经济 思享 青春 爱情 成长 文学 小说 美国 历史 情感 人生'
# list1 = str1.split(' ')
# tum1 = enumerate(list1)
# print(tuple(tum1))

# str2 ='小说 文学 人文社科 经济管理 科技科普 计算机于互联网 成功励志 生活 少儿 艺术设计 漫画绘本 教育考试 杂志'
# list2 = str2.split(' ')
# tum2 = enumerate(list2)
# print(tuple(tum2))

# FIRST_CATEGORY_LIST = ((0, '小说'), (1, '文学'), (2, '人文社科'), (3, '经济管理'), (4, '科技科普'), (5, '计算机于互联网'),
#                        (6, '成功励志'), (7, '生活'), (8, '少儿'), (9, '艺术设计'), (10, '漫画绘本'), (11, '教育考试'), (12, '杂志'))
#
#
# category = []
# for i in range(len(FIRST_CATEGORY_LIST)):
#     category.append(FIRST_CATEGORY_LIST[i][1])
# print(category)
# print(FIRST_CATEGORY_LIST[0][1])
# print(FIRST_CATEGORY_LIST[1][1])

# 测试函数修改全局列表，全局变量变化吗
# lst = [1,2,3,4,5,6]
#
# def func():
#     lst = []
#     print(lst)
# func()
# print(lst)


# str1 = '古典 投资 短篇 文化 政治 大家小书 心理学 旅行 恋爱 书单 三毛 学习 中篇 经典 长篇 诗词 创业 阅读 文艺 散文 哲学 下载 外国文学 人物 日本 心灵 励志 生活 合集 中国 必读 随笔 社会 英国 经济 思享 青春 爱情 成长 文学 小说 美国 历史 情感 人生'
# list1 = str1.split(' ')
# for i in list1:
#     print(i)


# import os
#
# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ebook_mall.settings")
#
#     import django
#     django.setup()
#
#     from Book import models
#     # # 一对一跨表查询
#     # brief = models.Book.objects.first().bookdetail.brief
#     # print(brief)
#     #
#     # title = models.BookDetail.objects.first().book.title
#     # print(title)
#
#     # 标签查找
#     tag = models.Tag.objects.filter(id=1)
#     book_obj =models.Book.objects.filter(book_tag=tag)
#     print(tag)
#     print(book_obj)

from random import choice
# def classcolour():
#     c_list = ["label label-success", "label label-warning", "label label-danger", "label label-info", "label label-active"]
#     value = choice(c_list)
#     return value
#
# print(classcolour())

# from random import choice
# def classcolour(value):
#     return "{}{}".format(value,choice(["label label-success", "label label-warning", "label label-danger", "label label-info", "label label-active"]))
#
# print(classcolour(''))