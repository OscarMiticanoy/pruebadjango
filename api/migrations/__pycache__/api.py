from rest_framework.response import Response
from .serializers import Users
from rest_framework.views import APIView
from rest_framework import status

class UserApi(APIView):
    def post(self, request):
        serializer = Users(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data==status.HTTP_201_CREATED)
        else:
            return Response(serializer.data==status.HTTP_400_BAD_REQUEST)