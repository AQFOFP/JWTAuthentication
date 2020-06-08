## JWTAuthentication
基于rest_framework下使用jwt进行认证



```python
# 1. 路由：
# urls.py
from user import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^order/$', views.OrderView.as_view()),
]


# views.py

class LoginView(APIView):
    authentication_classes = []  # 设置为空表示该接口不需要认证

    def post(self, request, *args, **kwargs):
        """ 用户登录 """
        user = request.POST.get('username')
        pwd = request.POST.get('password')

        # 检测用户和密码是否正确，此处可以在数据进行校验。
        user = UserInfo.objects.filter(username=user, password=pwd).first()
        if user:
            # 用户名和密码正确，给用户生成token并返回
            token = create_token({'userid': user.id, 'username': user.username})
            return Response({'status': True, 'token': token})
        return Response({'status': False, 'error': '用户名或密码错误'})
    
    
    
class OrderView(APIView):
    # 通过url传递token, #全局已经配置
    # authentication_classes = [JwtQueryParamAuthentication, ]

    # 通过Authorization请求头传递token
    # authentication_classes = [JwtAuthorizationAuthentication, ]

    def get(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '订单列表'})

    def post(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '添加订单'})

    def put(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '修改订单'})

    def delete(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '删除订单'})    
    
    
# settings    
REST_FRAMEWORK = {

    # 全局认证类
    'DEFAULT_AUTHENTICATION_CLASSES': ['user.utils.auth.JwtQueryParamAuthentication', 'user.utils.auth.JwtAuthorizationAuthentication']
}
```



## 登录获取token

![1591610449466](README\1591610449466.png)



## 请求需要认证的接口

![1591610585174](README\1591610537977.png)
