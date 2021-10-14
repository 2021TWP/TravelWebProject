from django.db import models


# 카테고리
from account.models import AccountInfo
from schedule.models import Schedule


class Category(models.Model):
    objects = models.Manager()
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


# 게시글
class Board(models.Model):
    objects = models.Manager()
    username = models.ForeignKey(AccountInfo, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    imgUrl = models.TextField()
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    board_content = models.TextField()
    hit = models.IntegerField()
    like = models.IntegerField()

    def __str__(self):
        return self.title


# 댓글
class Comment(models.Model):
    objects = models.Manager()
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    user_id = models.ForeignKey(AccountInfo, on_delete=models.CASCADE)
    comment_content = models.TextField()
    comment_date = models.DateTimeField()

    def __str__(self):
        return self.comment_content
