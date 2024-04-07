from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Bird, Feeding, Specie
from .serializers import BirdSerializer, FeedingSerializer, SpecieSerializer
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        species_not_assosiated = Specie.objects.exclude(id__in=instance.species.all())
        species_serializer = SpecieSerializer(species_not_assosiated, many=True)

        return Response({
            'bird': serializer.data,
            'species_not_associated': species_serializer.data
        })


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


class SpecieListCreate(generics.ListCreateAPIView):
   serializer_class = SpecieSerializer
   queryset = Specie.objects.all()


class SpecieDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpecieSerializer
    queryset = Specie.objects.all()
    lookup_field = 'id'


class AddSpecieToBird(APIView):
    def post(self, request, bird_id, specie_id):
        bird = Bird.object.get(id=bird_id)
        specie = Specie.objects.get(id=specie_id)
        bird.species.add(specie)
        return Response({'message': f'Bird {specie.name} added to bird {bird.name}'})
    
class RemoveSpecieFromBird(APIView):
    def post(self, request, bird_id, specie_id):
        bird = Bird.objects.get(id=bird_id)
        specie = Specie.objects.get(id=specie_id)
        bird.species.remove(specie)

        return Response({'message': f'Specie {specie.name} removed from Bird {bird.name}'})