from rest_framework.decorators import api_view
from rest_framework.response import Response
from board.models import Category, Board, Comment
from board.serializer import CategorySerializer, BoardSerializer, CommentSerializer , BoardCommentSerializer


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def board_free(request):
    boards = Board.objects.filter(category_id=1)
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def board_review(request):
    boards = Board.objects.filter(category_id=2)
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def board_impromptu(request):
    boards = Board.objects.filter(category_id=3)
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def board_list(request):
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def board_detail(request, pk):
#     board = Board.objects.get(id=pk)
#     # comments = Comment.objects.filter(id=board.id)
#     serializer = BoardCommentSerializer(board, many=False)
#     print(serializer.data)
#     return Response(serializer.data)
#     # return Response(serializer.data)

@api_view(['GET'])
def board_detail(request, pk):
    board = Board.objects.get(id=pk)
    serializer = BoardSerializer(board, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def board_create(request):
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Created!"})
    else:
        # return Response({"message": "Failed to create!"})
        return Response(request.data)


@api_view(['PUT'])
def board_update(request, pk):
    board = Board.objects.get(id=pk)
    serializer = BoardSerializer(instance=board, data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Updated!"})
    else:
        # return Response({"message": "Failed to update!"})
        return Response(serializer.data)


# @api_view(['PUT'])
# def board_update(request, pk):
#     board = Board.objects.get(id=pk)
#     serializer = BoardSerializer(instance=board, data=request.data)
#     print(request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Updated!"})
#     else:
#         # return Response({"message": "Failed to update!"})
#         return Response(serializer.data)


@api_view(['DELETE'])
def board_delete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return Response({"message": "Deleted!"})


@api_view(['PUT'])
def board_hit(request, pk):
    board = Board.objects.get(id=pk)
    serializer = BoardSerializer(instance=board, data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"message": "Failed to update Hit!"})


# @api_view(['PUT'])
# def board_like(request, pk):
#     board = Board.objects.get(id=pk)
#     serializer = BoardSerializer(instance=board, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Updated Like!"})
#     else:
#         return Response({"message": "Failed to update Like!"})


@api_view(['GET'])
def comment_list(request, bid):
    comments = Comment.objects.filter(board_id=bid)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request, pk):
    comments = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comments, many=False)
    return Response(serializer.data)


# @api_view(['POST'])
# # def comment_create(request, pk):
# def comment_create(request, pk):
#
#     board = Board.objects.get(id=pk)
#     serializer = CommentSerializer(instance=board, data=request.data)
#     if serializer.is_valid():
#         # serializer.save(board=board)
#         serializer.save()
#         return Response({"message": "Created!"})
#     else:
#         return Response({"message": "Failed to create!"})


@api_view(['POST'])
def comment_create(request):
    serializer = CommentSerializer(data=request.data)
    print("코멘트 데이터 ========> ", request.data)
    if serializer.is_valid():
        # print("true data ==== ", serializer.data)
        serializer.save()
        return Response({"message": "Created!"})
    else:
        print("fail data ==== ", serializer.is_valid)
        # return Response({"message": "Failed to create!"})
        return Response(serializer.data)


@api_view(['PUT'])
def comment_update(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data)
    print("코멘트 데이터 ========> ", request.data)
    if serializer.is_valid():
        serializer.save()
        print("success")
        # return Response({"message": "Updated!"})
        return Response(serializer.data)
    else:
        print("fail")
        return Response(serializer.data)

        # return Response({"message": "Failed to update!"})


@api_view(['DELETE'])
def comment_delete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return Response({"message": "Deleted!"})
