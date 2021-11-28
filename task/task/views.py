from django.db.models import fields
from .models import User,Group
from django.http import HttpResponse,JsonResponse
from django.utils import timezone
from django.core import serializers
import json
from jsonschema import validate
from .schema import user_schema


        
def user_schema_validation(data):
    try:
        validate(data,user_schema)
    except:
        return False

#########  user part
def user_add(request):
    user_data = json.loads(request.body)
    print(user_data)

    try:
        User.objects.create(
            username = user_data['username'],
            email = user_data['email'],
            is_admin = user_data['is_admin'],
            date_added = timezone.now()
        )
    except:
        print('Error in creating user')
        return HttpResponse(status=400)
    return HttpResponse(status=200)



def get_users(request):
    users = User.objects.all()
    response = []

    for user in users:
        grps = user.group_set.all()
        grps = [g.name for g in grps]
        u = {
            'id':user.id,
            'username': user.username,
            'email': user.email,
            'is_admin': user.is_admin,
            'date_added': str(user.date_added),
            'groups': grps,
        }
        response.append(u)
    response = json.dumps(response)
    return HttpResponse(response)

def user_edit(request,id):
    user_data = json.loads(request.body)
    try:
        user = User.objects.get(id=id)
        user.username = user_data['username']
        user.email = user_data['email']
        user.is_admin = user_data['is_admin']
        user.date_edited = timezone.now()
        user.save()
    except:
        print('error with editing user')
        return(HttpResponse(status=400))
    return(HttpResponse(status = 200))
    

def delete_user(request,id):
    User.objects.filter(id=id).delete()
    return HttpResponse(status=200)


######## group part

def add_group(request):
    group_data = json.loads(request.body)
    group = Group(
        name = group_data['name'],
        description = group_data['description'],
        work_names = '0000'
    )
    group.save()
    users_to_add = group_data['users_to_add'] # their usernames
    users = User.objects.filter(id__in = users_to_add)
    for user in users:
        group.users_to_groups.add(user.id)
        # print(user.group_set.all())
    return JsonResponse(data={'status':200})


def edit_group(request,id):
    try:
        group_data = json.loads(request.body)
        group = Group.objects.get(id=id)
        group.name = group_data['name']
        group.description = group_data['description']
        users = User.objects.filter(id__in = group_data['group_users'])
        group.users_to_groups.clear()
        for user in users:
            group.users_to_groups.add(user.id)
        group.save()
    except Exception:
        print('EXEPTION IN EDITING GROUP')
        JsonResponse(data={'status':400})
    return JsonResponse(data={'status':200})

def get_groups(request):
    response = []
    try:
        groups = Group.objects.all()
        for group in groups:
            users = group.users_to_groups.all()
            users = [[u.id, u.username] for u in users]
            grp = {
                'id':group.id,
                'name': group.name,
                'description': group.description,
                'work_names': group.work_names,
                'users': users,
            }
            response.append(grp)
        response = json.dumps(response)
    except Exception:
        print('EXEPTION IN RETURNING GROUPS')
        return(JsonResponse(data={'status': 404}))
    return HttpResponse(response)

def delete_group(request,id):
    group = Group.objects.get(id=id)
    if len(group.users_to_groups.all()) > 0:
        return JsonResponse(data={'response':'Group is not empty'})
    try:
        group.delete()
    except:
        JsonResponse(data={'response':'ERROR'})
    return JsonResponse(data={'response':'ok'})

def set_work_names(request):
    works = json.loads(request.body)
    group = Group.objects.get(id=works['id'])
    works = ''.join([str(int(w)) for w in works['work_names']])
    group.work_names = works
    group.save()
    return HttpResponse(status = 200)
    






    
    