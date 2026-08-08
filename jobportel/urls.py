"""
URL configuration for jobportel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Landing page: shows the login form. Already-logged-in users are sent
    # straight to the job list (see redirect_authenticated_user below).
    path(
        "",
        LoginView.as_view(
            template_name="login.html",
            redirect_authenticated_user=False,
        ),
        name="home",
    ),
    path("job/", include("job.urls"), name="job"),
    path("accounts/", include("accounts.urls"), name="accounts"),
]
