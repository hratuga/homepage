from rest_framework import status, viewsets, mixins
from .models import *
from .serializers import *

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class PackingListTagViewSet(viewsets.ModelViewSet):
    queryset = PackingListTag.objects.all()
    serializer_class = PackingListTagSerializer


class PackingListViewSet(viewsets.ModelViewSet):
    queryset = PackingList.objects.all()
    serializer_class = PackingListSerializer


class PackingListItemViewSet(viewsets.ModelViewSet):
    queryset = PackingListItem.objects.all()
    serializer_class = PackingListItemSerializer


class NewsBoxViewSet(viewsets.ModelViewSet):
    queryset = NewsBox.objects.all()
    serializer_class = NewsBoxSerializer
