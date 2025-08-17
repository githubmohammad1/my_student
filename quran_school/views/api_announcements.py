from rest_framework import generics
from ..models import Announcement
from ..serializers import AnnouncementSerializer

class AnnouncementListCreateAPI(generics.ListCreateAPIView):
    queryset = Announcement.objects.all().order_by('-created_at')
    serializer_class = AnnouncementSerializer

class AnnouncementDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
