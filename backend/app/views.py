from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from django.middleware.csrf import get_token

from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import UserSerializer, GroupSerializer


def home_view(request):
    return render(request, "index.html", {})


def csrf_token_view(request):
    return JsonResponse({"csrftoken": get_token(request)})


# Regular function view, available only to logged_in users
def auth_view(request):
    return JsonResponse({"isAuthenticated": request.user.is_authenticated})


@login_required
def protected_view(request):
    ctx = {
        "userInfo": {
            "userId": request.user.id,
            "role": "Admin",
            "userUrl": f"{reverse('admin:auth_user_changelist')}{request.user.id}",
            "firstName": request.user.first_name,
            "lastName": request.user.last_name,
            "email": request.user.email,
            "isActive": request.user.is_active,
            "dateJoined": request.user.date_joined,
        }
    }
    return JsonResponse(ctx)


# DRF - viewsets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
