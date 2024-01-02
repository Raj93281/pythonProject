from rest_framework import serializers
from .models import CustomUser, UserGroup, Event, EventInvitation


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'availability']

class UserGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserGroup
        fields = ['unique_identifier', 'name', 'members']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'time']

class EventInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventInvitation
        fields = ['event', 'invited_user', 'response']
