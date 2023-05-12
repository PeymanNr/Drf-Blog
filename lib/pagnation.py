from rest_framework.pagination import PageNumberPagination, CursorPagination


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 5


class StandardPagination(CursorPagination):
    ordering = 'post_id'
