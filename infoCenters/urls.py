from django.urls import path,include
from django.conf.urls import url, re_path
from .views import *
from rest_framework.routers import DefaultRouter
from .viewset import *
from django.views.static import serve
from INFOCENTER.settings import MEDIA_ROOT, STATIC_ROOT

router = DefaultRouter()

router.register(r'allNews', PassageViewSet)
router.register(r'allImages', DMViewSet)
router.register(r'allVedio', VedioViewSet)
router.register(r'allBarData', BarModelViewSet)
router.register(r'allLineData', LineModelViewSet)
router.register(r'allPieData', PieModelViewSet)
router.register(r'allMixData', MixModelViewSet)
router.register(r'allMagazine', MagazineViewSet)

app_name = 'career'
urlpatterns = [
    path('', index),
    url(r'allnews/(\d+)?$', allNews, name='allnews'),
    path('index', indexChange, name='index'),
    path('news/<str:i>', news),
    url(r'imgDisplay/(\d+)?$', imgDisplay),
    url(r'allvedio/(\d+)?$', vediolist),
    path('vedio/<str:page>', vedio),
    path('contactus', contactus, name='contactus'),
    url(r'dataDisplay/(\d+)?$', dataDisplay),
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    re_path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),


    path('API/', include(router.urls)),

    path('success',Success,name ='success')
]
