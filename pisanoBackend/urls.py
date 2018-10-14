from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from appDatas import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pills/$', views.PillList.as_view()),
    url(r'^pills/(?P<pk>[0-9]+)/$', views.PillDetailById.as_view()),
    url(r'^pills/(?P<title>[\w-]+)/$', views.PillDetailByTitle.as_view()),
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetailById.as_view()),
    url(r'^products/(?P<title>[\w-]+)/$', views.ProductDetailByTitle.as_view()),
    url(r'^pharmacies/$', views.PharmacyList.as_view()),
    url(r'^pharmacies/(?P<pk>[0-9]+)/$', views.PharmacyDetailById.as_view()),
    url(r'^pills/(?P<title>[\w-]+)/$', views.PharmacyDetailByTitle.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)