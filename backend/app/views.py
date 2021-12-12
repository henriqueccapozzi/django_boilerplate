from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import UserSerializer, GroupSerializer


def home_view(request):
    return render(request, "index.html", {})


# Regular function view, available only to logged_in users
@login_required
def protected_view(request):
    ctx = {
        "userInfo": {
            "userId": f"{reverse('admin:auth_user_changelist')}{request.user.id}",
            "firstName": request.user.first_name,
            "lastName": request.user.last_name,
            "email": request.user.email,
            "isActive": request.user.is_active,
            "dateJoined": request.user.date_joined,
        }
    }
    return render(request, "dashboard.html", ctx)


# DRF - viewsets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
