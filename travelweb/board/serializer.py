from rest_framework import serializers
from board.models import Category, Board, Comment

from authentication.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class BoardSerializer(serializers.ModelSerializer):
    # schedule_id = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='board_detail')

    class Meta:
        model = Board
        fields = ['id', 'user_id', 'category_id', 'title', 'imgUrl',
                  'schedule_id', 'date', 'board_content', 'hit', 'like']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'board_id', 'user_id', 'comment_content', 'comment_date']


class BoardCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    boards = BoardSerializer(many=True, read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'user_id', 'category_id', 'title', 'imgUrl',
                  'schedule_id', 'date', 'board_content', 'hit', 'like', 'comments', 'board', 'users']

    def create(self,validated_date) :
        pass
