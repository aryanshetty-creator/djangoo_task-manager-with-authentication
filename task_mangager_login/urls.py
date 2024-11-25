"""
URL configuration for task_mangager_login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from tasks import views as task_views  # Import views from the `tasks` app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),  # Include task app's URLs
    path('login/', task_views.login_view, name='login'),  # Assuming a login view exists in tasks app
    path('logout/', task_views.logout_view, name='logout'),  # Assuming a logout view exists
    path('', task_views.home, name='home'),  # Root URL points to the home view
]


