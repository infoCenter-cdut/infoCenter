from rest_framework import pagination
#以下是分页设置
class PassagePagination(pagination.PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'  # 每页的数量
    page_query_param = "passage"
    max_page_size = 10

class DMPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 每页的数量
    page_query_param = "dmImg"
    max_page_size = 10


class VedioPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'  # 每页的数量
    page_query_param = "vedio"
    max_page_size = 10


class MagazinePagination(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = 'magazine_size'
    page_query_param = 'magazine'
    max_page_size = 10


class BarModelPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_description = 'page_size'
    page_query_param = "Nothing"
    max_page_size = 50


class LineModelPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_description = 'page_size'
    page_query_param = "Nothing"
    max_page_size = 50


class PieModelPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_description = 'page_size'
    page_query_param = "Nothing"
    max_page_size = 50


class MixModelPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_description = 'page_size'
    page_query_param = 'mixData'
    max_page_size = 50