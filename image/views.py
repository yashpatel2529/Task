from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer



class Profile(APIView):

    def get(self):
        result = User.objects.all()
        serializers = UserSerializer(result, many=True)
        return Response({"Details": serializers.data}, )