import xadmin

# Register your models here.
from .models import Article,Course


class CourseAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['content']
    search_fields = ['content']
    list_editable = ['content']
    list_filter = ['content']


class ArticleAdmin(object):
    list_display = ['article_id', 'title', 'brief_content', 'content', 'publish_date',
                    'title']
    search_fields = ['article_id', ]
    list_editable = ['article_id', 'title', 'brief_content', 'content', 'publish_date']
    list_filter = ['article_id', 'title', 'brief_content', 'content', 'publish_date']


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Course, CourseAdmin)