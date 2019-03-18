from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
     url('^$',views.welcome,name = 'welcome'),
     url(r'^image/(\d+)',views.image,name ='image'),
    #  url(r'^$',views.all_image,name='all_Images'), 
     url(r'^search/', views.search_results, name='search_results'),
     url(r'^searchs/', views.search_result, name='search_result')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)