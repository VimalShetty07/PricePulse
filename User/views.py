from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import UserSerilizer
from rest_framework.response import Response


# view for registering users
class register(APIView):
    def post(self, request):
        serializer = UserSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


def login(request):
    return HttpResponse("Hello world!")


def logout(request):
    return HttpResponse("Hello world!")
