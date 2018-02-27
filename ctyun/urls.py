from django.contrib import admin
from django.conf.urls import include,url
from home import views as home_view


urlpatterns = [
    url('admin/', admin.site.urls),
    url('dns/', include('dns.urls')),

    # url(r'^accounts/login/$', LoginView.as_view()),
    # url(r'^accounts/logout/$', LogoutView.as_view(next_page='/')),
    # 测试自定义用户验证
    url(r'^login/$', home_view.login_view),
    url(r'^logout/$', home_view.logout_view),
    url(r'^$', home_view.index),  # 总的index页面入口
]
