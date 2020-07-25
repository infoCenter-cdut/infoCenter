#以下是视图类的配置
from rest_framework import mixins, viewsets
from .pagination import *
from .serializers import *
'''
    以下是对应接口的设置，接口等待2.0版本使用
'''

class DMViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
     '''
     List all DM papers
     '''
     queryset = DMIMG.objects.all().order_by('-id')
     serializer_class = DMSerializer

    
class PassageViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    List all Passage
    '''
    queryset = Passage.objects.all().order_by('-passage_time')
    serializer_class = PassageSerializer
    pagination_class = PassagePagination

class VedioViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    List all Vedio
    '''

    queryset = Vedio.objects.all().order_by('-vedio_time')
    serializer_class = VedioSerializer
    pagination_class = VedioPagination

    def get_queryset(self):
        return self.queryset

class MagazineViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    List all magazine
    '''
    queryset = Magazine.objects.get_queryset().order_by('-id')
    serializer_class = MagazineSerializer
    pagination_class = MagazinePagination

class BarModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    List all data of bar
    '''
    queryset = BarModel.objects.all().order_by('-bar_time')
    serializer_class = BarModelSerializer
    pagination_class = BarModelPagination

class LineModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    List all data of line
    '''
    queryset = LineModel.objects.all().order_by('-line_time')
    serializer_class = LineModelSerializer
    pagination_class = LineModelPagination

class PieModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    List all data of pie
    '''
    queryset = PieModel.objects.all().order_by('-pie_time')
    serializer_class = PieModelSerializer
    pagination_class = PieModelPagination

class MixModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    List all mix data
    '''
    queryset = MixModel.objects.all().order_by('-mix_time')
    serializer_class = MixModelSerializer
    pagination_class = MixModelPagination
