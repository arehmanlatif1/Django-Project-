from rest_framework import serializers
from .models import Bird, Feeding

class BirdSerializer(serializers.ModelSerializer):
    fed_for_today = serializers.SerializerMethodField()
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
