from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_list,
    bc_create,
    post_detail,
    bc_update,
    bc_delete,
    bc_postlist,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^backend/$', bc_postlist, name='bclist'),
    url(r'^backend/create/$', bc_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', bc_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', bc_delete),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
]
