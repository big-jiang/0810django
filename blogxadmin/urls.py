from django.urls import path

import blogxadmin.views

urlpatterns = [
    path("hello_world", blogxadmin.views.hello_world),
    path("content", blogxadmin.views.article_content),
    path("index", blogxadmin.views.get_index_page),
    path("detail/<int:article_id>", blogxadmin.views.get_detail_page),
    path("edit", blogxadmin.views.edit),
    path("saveEdit", blogxadmin.views.saveEdit),
    path("test", blogxadmin.views.test),
]