from django.urls import path
from .views import (
    my_profile_view,
    invites_received_view,
    ProfileDetailView,
    ProfileListView,
    send_invatation,
    remove_from_friends,
    accept_invatation,
    reject_invatation,
    FriendListView
)

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name = 'my-profile-view'),
    path('my-invites/', invites_received_view, name = 'my-invites-view'),
    path('', ProfileListView.as_view(), name = 'all-profiles-view'),
    path('friends/', FriendListView.as_view(), name = 'all-friends-view'),
    path('send-invite/', send_invatation, name = 'send-invite'),
    path('remove-friend/', remove_from_friends, name = 'remove-friend'),
    path('<slug>/', ProfileDetailView.as_view(), name = 'profile-detail-view'),
    path('my-invites/accept/', accept_invatation, name = 'accept-invite'),
    path('my-invites/reject/', reject_invatation, name='reject-invite'),
]

