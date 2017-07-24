"""backend URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django_cas_ng import views

urlpatterns = [
    # OAuth 2 endpoints:
    url(r'^admin/', admin.site.urls),
    url(r'^', include('account.urls')),
    url(r'^', include('kenalan.urls')),
    url(r'^', include('website.urls')),
    url(r'^login/$', views.login, name='cas_ng_login'),
    url(r'^logout$', views.logout, name='cas_ng_logout'),
    url(r'^callback$', views.callback, name='cas_ng_proxy_callback'),
    url(r'^docs/', include('rest_framework_docs.urls')),

]