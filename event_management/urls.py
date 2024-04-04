from django.urls import path
from .views import CustomUserListCreateView,UserGroupListCreateView,UserGroupDetailView,CreateEventView,EventInvitationView, FreeuserView,ProductList,CartItemList,LandingPageView

urlpatterns = [
    path('create-user/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('user-groups/', UserGroupListCreateView.as_view(), name='usergroup-list'),
    path('user-groups/<str:unique_identifier>/', UserGroupDetailView.as_view(), name='usergroup-detail'),
    path('Creat-Event/',CreateEventView.as_view(), name='create-event'),
    path('Event-Invitation/',EventInvitationView.as_view(), name='evebt-invitation'),
    path('free-user-list/',FreeuserView.as_view(), name= 'free-user-list'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('cart/', CartItemList.as_view(), name='cart-list'),
    path('landing/',LandingPageView.as_view(), name='landing-page')
]
