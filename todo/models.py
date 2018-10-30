from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField('제목', max_length=255)
    content = models.TextField('내용')

    def __str__(self):
        return self.title
