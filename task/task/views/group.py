from ..models import User, Group
from ..validations import group_schema_validation
from django.http import HttpResponse, JsonResponse
import json


def add_group(request):
    group_data = json.loads(request.body)
    if group_schema_validation(group_data) == 'not valid':
        return HttpResponse(status=400)
    group = Group(
        name=group_data['name'],
        description=group_data['description'],
        work_names='0000'
    )
    group.save()
    users_to_add = group_data['users_to_add']  # their usernames
    users = User.objects.filter(id__in=users_to_add)
    for user in users:
        group.users_to_groups.add(user.id)
    return JsonResponse(data={}, status=200)


def edit_group(request, id):
    group_data = json.loads(request.body)
    if group_schema_validation(group_data) == 'not valid':
        return HttpResponse(status=400)
    try:
        group = Group.objects.get(id=id)
        group.name = group_data['name']
        group.description = group_data['description']
        users = User.objects.filter(id__in=group_data['users_to_add'])
        group.users_to_groups.clear()
        for user in users:
            group.users_to_groups.add(user.id)
        group.save()
    except Exception as exp:
        print(exp)
        JsonResponse(data={}, status=400)
    return JsonResponse(data={}, status=200)


def get_groups(request):
    response = []
    try:
        groups = Group.objects.all()
        for group in groups:
            users = group.users_to_groups.all()
            users = [[u.id, u.username] for u in users]
            grp = {
                'id': group.id,
                'name': group.name,
                'description': group.description,
                'work_names': group.work_names,
                'users': users,
            }
            response.append(grp)
        response = json.dumps(response)
    except Exception as exp:
        print(exp)
        return JsonResponse(data={}, status=400)
    return HttpResponse(response)


def delete_group(request, id):
    group = Group.objects.get(id=id)
    if len(group.users_to_groups.all()) > 0:
        return JsonResponse(data={'response': 'Group is not empty'})
    try:
        group.delete()
    except Exception as exp:
        print(exp)
        JsonResponse(data={}, status=400)
    return JsonResponse(data={'response': 'ok'}, status=200)


def set_work_names(request):
    try:
        works = json.loads(request.body)
        group = Group.objects.get(id=works['id'])
        works = ''.join([str(int(w)) for w in works['work_names']])
        group.work_names = works
        group.save()
    except Exception as exp:
        print(exp)
        return HttpResponse(status=400)
    return HttpResponse(status=200)
