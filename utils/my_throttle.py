from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect
from django.conf import settings
import time


ACCESS_RECORD = {}
# 自定义访问频率限制的中间件
class ThrottleMiddleware(MiddlewareMixin):

    def process_request(self,request):
        access_limit = settings.ACCESS_LIMIT if hasattr(settings, 'ACCESS_LIMIT') else 60
        # 当前请求的IP地址
        ip = request.META.get('REMOTE_ADDR')
        if ip not in ACCESS_RECORD:
            ACCESS_RECORD[ip] = []
        history = ACCESS_RECORD[ip]
        # 判断最近的10秒钟之内这个IP访问次数是否大于3
        now = time.time()
        # DRF 访问频率限制
        while history and now - history[-1] > access_limit:
            history.pop()

        history.insert(0, now)
        access_rate = settings.ACCESS_RATE if hasattr(settings,'ACCESS_RATE') else 30
        if len(history) > access_rate:
            return HttpResponse('您的访问过于频繁，请%s秒后再试' % access_limit)



# 自定义登陆验证的中间件
# class CheckLogin(MiddlewareMixin):
#
#     def process_request(self,request):
#         # 判断当前访问的URL是不是在白名单中
#         white_urls = settings.WHITE_URLS if hasattr(settings.WHITE_URLS) else []
#         if request.path_info in white_urls:
#             return None
#         # 从请求的session数据中取user
#         user_id = request.session.get('user',None)
#         if not user_id:
#             # 没有登陆跳转到登陆页面
#             return redirect('/login/')
#         else:
#             user_obj = UserInfo.objects.get(id=user_id)
#             request.user = user_obj