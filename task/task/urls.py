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
from .views import group, user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/add-user/', user.user_add),
    path('users/edit-user/<int:id>/', user.user_edit),
    path('users/', user.get_users),
    path('users/delete/<int:id>/', user.delete_user),

    path('groups/add-group/', group.add_group),
    path('groups/', group.get_groups),
    path('groups/delete/<int:id>/', group.delete_group),
    path('groups/work-names/', group.set_work_names),
    path('groups/edit-group/<int:id>/', group.edit_group)
]
