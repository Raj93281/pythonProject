from rest_framework import generics
from django.shortcuts import render
from .models import CustomUser, UserGroup, Event,EventInvitation,Product,CartItem, Employee
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import CustomUserSerializer,UserGroupSerializer, EventSerializer, EventInvitationSerializer,ProductSerializer,CartItemSerializer,EmployeeSerializer

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

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class LandingPageView(generics.CreateAPIView):
    def get(self, request):
        context = {"message": "Welcome to the karma tecnologies!"}
        return render(request, 'index.html', context)

class empView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def emp(request):
        if request.method == "POST":
            serializer = EmployeeForm(request.POST)
            if serializer.is_valid():
                try:
                    serializer.save()
                    return redirect('/show')
                except:
                    pass
        else:
            serializer = EmployeeSerializer()
        return render(request,'index.html',{'form':form})
class showdetailsView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    def show(request):
        employees = Employee.objects.all()
        return render(request,"show.html",{'employees':employees})

class editdetailsView(generics.CreateAPIView):
    def edit(request, id):
        employee = Employee.objects.get(id=id)
        return render(request,'edit.html', {'employee':employee})

class updatedetailsView(generics.UpdateAPIView):
    def update(request, id):
        employee = Employee.objects.get(id=id)
        serializer = EmployeeForm(request.POST, instance = employee)
        if serializer.is_valid():
            serializer.save()
            return redirect("/show")
        return render(request, 'edit.html', {'employee': employee})

class deletedetailsView(generics.DestroyAPIView):
    def destroy(request, id):
        employee = Employee.objects.get(id=id)
        employee.delete()
        return redirect("/show")



