from ..models import User
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from ..validations import user_schema_validation
import json


def user_add(request):
    user_data = json.loads(request.body)
    if user_schema_validation(user_data) == 'not valid':
        return HttpResponse(status=400)
    try:
        User.objects.create(
            username=user_data['username'],
            email=user_data['email'],
            is_admin=user_data['is_admin'],
            date_added=timezone.now()
        )
    except Exception as exp:
        print(exp)
        return HttpResponse(status=400)
    return HttpResponse(status=200)


def get_users(request):
    users = User.objects.all()
    response = []

    for user in users:
        groups = user.group_set.all()
        groups = [g.name for g in groups]
        u = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_admin': user.is_admin,
            'date_added': str(user.date_added),
            'groups': groups,
        }
        response.append(u)
    response = json.dumps(response)
    return HttpResponse(response)


def user_edit(request, id):
    user_data = json.loads(request.body)
    if user_schema_validation(user_data) == 'not valid':
        return HttpResponse(status=400)
    try:
        user = User.objects.get(id=id)
        user.username = user_data['username']
        user.email = user_data['email']
        user.is_admin = user_data['is_admin']
        user.date_edited = timezone.now()
        user.save()
    except Exception as exp:
        print(exp)
        return HttpResponse(status=400)
    return HttpResponse(status=200)


def delete_user(request, id):
    try:
        User.objects.filter(id=id).delete()
    except Exception as exp:
        print(exp)
        return HttpResponse(status=400)
    return HttpResponse(status=200)
