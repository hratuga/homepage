# serializers.py
from rest_framework import serializers
from .models import *

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'

class PackingListTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingListTag
        fields = '__all__'

class PackingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingList
        fields = '__all__'


class PackingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingListItem
        fields = '__all__'



class NewsBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsBox
        fields = '__all__'

