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
from account import cas_views
from django.conf import settings
from django.conf.urls.static import static
from account.utils import SSOAuth
from website.utils import update_user_statistic

urlpatterns = [
    # OAuth 2 endpoints:
    url(r'^pmb-api/$', SSOAuth.as_view()),
    url(r'^pmb-api/admin/', admin.site.urls),
    url(r'^pmb-api', include('account.urls')),
    url(r'^pmb-api', include('kenalan.urls')),
    url(r'^pmb-api', include('website.urls')),
    url(r'^pmb-api/login/$', cas_views.login, name='cas_ng_login'),
    url(r'^pmb-api/logout$', cas_views.logout, name='cas_ng_logout'),
    url(r'^pmb-api/callback$', cas_views.callback, name='cas_ng_proxy_callback'),
    url(r'^pmb-api/docs/', include('rest_framework_docs.urls')),
    url(r'^pmb-api/update-user-statistic/', update_user_statistic),

]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
