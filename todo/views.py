from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo


def todo_json(todo):
    return {
        'id': todo.id,
        'title': todo.title,
        'detail': todo.detail,
        'completed': todo.completed,
        'updated_at': todo.updated_at,
        'created_at': todo.created_at
    }


class TodoAPI(APIView):

    @csrf_exempt
    def get(self, request):
        return Response([todo_json(t) for t in Todo.objects.all()], status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request):
        if not request.data.get('id'):
            todo = Todo.objects.create(title=request.data.get('title'),
                                       detail=request.data.get('detail'),
                                       completed=request.data.get('completed'))
            return Response(todo_json(todo), status=status.HTTP_200_OK)
        else:
            try:
                todo = Todo.objects.get(id=request.data.get('id'))
                todo.title = request.data.get('title')
                todo.detail = request.data.get('detail')
                todo.completed = request.data.get('completed')
                todo.save()
                return Response(todo_json(todo), status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response('', status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def delete(self, request):
        try:
            todo = Todo.objects.get(id=request.GET.get('id'))
            todo.delete()
            return Response('Deleted.', status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response('Failed.', status=status.HTTP_404_NOT_FOUND)
