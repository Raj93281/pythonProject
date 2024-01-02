from rest_framework import generics
from .models import CustomUser, UserGroup, Event,EventInvitation
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import CustomUserSerializer,UserGroupSerializer, EventSerializer, EventInvitationSerializer

class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserGroupListCreateView(generics.ListCreateAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

class UserGroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    lookup_field = 'unique_identifier'

class CreateEventView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventInvitationView(generics.CreateAPIView):
    queryset = EventInvitation.objects.all()
    serializer_class = EventInvitationSerializer

class FreeuserView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        date = self.request.query_params.get('date', None)

        if date is not None:
            # Filter users without events on the specified date
            free_users = EventSerializer.objects.exclude(user__event__date=date)
        else:
            # If no date is provided, return all users
            free_users = Event.objects.all()

        return free_users



