from django.conf.urls import include, url
from django.contrib import admin

from teacher import views as tv
from teacher import teacher_url

urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyuan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 视图函数名称只有名称，无括号和参数
    url(r'^normalmap/', tv.do_normalmap),


    # 尖号表示以后面内容开头的表达式
    # 圆括号表示的是一个参数，里面的内容作为参数传递给被调用的函数
    # 参数名称以问好加大写P开头，尖括号里面就是参数的名字
    # 尖括号后表示正则，[0-9]表示内容仅能是有0-9的数字构成，
    # 后面大括号表示出现的次数，此处4表示只能出现四个0-9的数字
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.withparam),  # 正常映射


    # 比如约定，凡是由teacher模块处理的视图的url都以teacher开头
    url(r'^teacher/', include(teacher_url)),

    url(r'^book/(?:page-(?P<pn>\d+)/)$', tv.do_param2),



    url(r'^yourname/$', tv.revParse, name="askname"),
]
