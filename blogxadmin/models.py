from django.db import models

from DjangoUeditor.models import UEditorField

from tinymce.models import HTMLField
# Create your models here.


class Course(models.Model):
    # detail = models.TextField("课程详情")
    content = UEditorField(verbose_name='内容', height=500, width=1000,
                           default=u'', imagePath="Article_img/%%Y/%%m/",
                           toolbars='full', filePath='Article_file/%%Y/%%m/',
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, command=None,)


class Article(models.Model):
    # 文章唯一性ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章主要内容
    content = HTMLField()
    # 文章发布的时间
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章阅读'
        verbose_name_plural = verbose_name