from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, "index.html", {})


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
