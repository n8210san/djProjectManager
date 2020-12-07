"""pLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

""" 2020 1128 練習
 https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/skeleton_website
"""
# Use include() to add paths from the catalog application
# include() 會在指定的結束字符處分割URL字符串，並將剩餘的子字符串發送到所包含的URLconf 模塊
from django.conf.urls import include
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
"""
我們使用一個特別的視圖函數( RedirectView)，當path()函數中的 url 式樣被識別以後
（在這個例子中是根 url），就會把第一個參數，也就是新的相對 URL ，重定向到（/catalog/）。
"""
# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/')),
]
"""Django默認不提供CSS，JavaScript和圖像等靜態文件"""
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

