from rest_framework import serializers
from .models import CustomUser, UserGroup, Event, EventInvitation, Product, CartItem


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

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'
