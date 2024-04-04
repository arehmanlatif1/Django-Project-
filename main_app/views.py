from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Bird, Feeding
from .serializers import BirdSerializer, FeedingSerializer
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

class FeedingListCreate(generics.ListCreateAPIView):
    serializer_class = FeedingSerializer

    def get_queryset(self):
        bird_id = self.kwargs['bird_id']
        return Feeding.objects.filter(bird_id=bird_id)
    
    def perform_create(self, serializer):
        bird_id = self.kwargs['bird_id']
        bird = Bird.objects.get(id=bird_id)
        serializer.save(bird=bird)

class FeedingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedingSerializer
    lookup_field = 'id'

    def get_queryset(self):
        bird_id = self.kwargs['bird_id']
        return Feeding.objects.filter(bird_id=bird_id)
