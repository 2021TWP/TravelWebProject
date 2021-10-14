from django.contrib import admin
from board.models import Category
from board.models import Board
from board.models import Comment


admin.site.register(Category)
admin.site.register(Board)
admin.site.register(Comment)
