from rest_framework import serializers
from .models import Bird, Feeding, Specie
from django.contrib.auth.models import User

class UserSerializater(serializers.ModelSerializer):
   password = serializers.CharField(write_only=True)

   class Meta:
      models = User
      fields = ('id', 'username', 'email')

   def create(self, validated_data):
       user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']

       )
       return user

class SpecieSerializer(serializers.ModelSerializer):
   class Meta: 
      model = Specie
      fields = '__all__'

class BirdSerializer(serializers.ModelSerializer):
    fed_for_today = serializers.SerializerMethodField()
    species = SpecieSerializer(many=True, read_only=True)

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Bird
        fields = '__all__'

    def get_fed_for_today(self, obj):
     return obj.fed_for_today()


class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
        read_only_fields = ('birds',)

