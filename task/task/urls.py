"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/add-user/', views.user_add),
    path('users/edit-user/<int:id>/',views.user_edit),
    path('users/', views.get_users),
    path('users/delete/<int:id>/',views.delete_user),
    
    path('groups/add-group/',views.add_group),
    path('groups/',views.get_groups),
    path('groups/delete/<int:id>/',views.delete_group),
    path('groups/work-names/',views.set_work_names),
    path('groups/edit-group/<int:id>/',views.edit_group)
]
