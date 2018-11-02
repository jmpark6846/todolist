from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    PRIORITY_CHOICES = (
        (1, '우선 순위 1'),
        (2, '우선 순위 2'),
        (3, '우선 순위 3'),
    )

    title = models.CharField('제목', max_length=255)
    content = models.TextField('내용')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    duedate = models.DateField('마감기한', blank=True, null=True)
    done = models.BooleanField('완료', default=False)
    priority = models.IntegerField('우선 순위', choices=PRIORITY_CHOICES, default=1)

    created = models.DateTimeField('생성날짜', auto_now_add=True)
    updated = models.DateTimeField('수정날짜', auto_now=True)

    def __str__(self):
        return self.title
