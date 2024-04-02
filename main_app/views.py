from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Bird
from .serializers import BirdSerializer
# Create your views here.

class Home(APIView):
    def get(self, request):
        content = {"message": "Welcome to bird-Collector API home route!"}
        return Response(content)
class BirdList(generics.ListCreateAPIView):
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer

class BirdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer
    lookup_field = 'id'