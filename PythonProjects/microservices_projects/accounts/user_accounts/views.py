import json
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from passlib.hash import sha256_crypt
from passlib.hash import pbkdf2_sha256


# Create your views here.


def home(request):
    response = 'Hello World!'
    return HttpResponse(response)


# @api_view(['POST'])
# def create_user(request):
#     import pdb; pdb.set_trace();
#     serializer = UserSerializer(data=request.Data)
#     if serializer.is_valid():
#         username = serializer.initial_data['username']
#         password = serializer.initial_data['password']
#         first_name = serializer.initial_data['first_name']
#         last_name = serializer.initial_data['last_name']
#         email = serializer.initial_data['email']
#
#
#
#     response = {'Welcome': 'Welcome to Django rest framework examples'}
#     response = json.dumps(response)
#     return HttpResponse(response, content_type="application/json")

@api_view(['POST'])
def create_user(request):
    import pdb; pdb.set_trace();
    if request.method == 'POST':
        serialized = UserSerializer(data=request.POST)
        if serialized.is_valid():
            user = User()
            user.username = request.POST.get('username')
            password = request.POST.get('password')
            # enc_password = sha256_crypt.encrypt(password)
            enc_password = pbkdf2_sha256.encrypt(password)
            user.password = enc_password
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.is_superuser = False
            user.is_staff = False
            user.save()
            content ={'result': 'User Created Successfully'}
            message = json.dumps(content)
            return HttpResponse(message, content_type='application/json')
        else:
            content = {'message': 'Invalid request'}
            error_message = json.dumps(content)
            return HttpResponse(error_message, content_type='application/json')
    else:
        content = {'message': 'Invalid request'}
        error_message = json.dumps(content)
        return HttpResponse(error_message, content_type='application/json')


@csrf_exempt
@api_view(['GET'])
def list_users(request):
    import pdb;
    pdb.set_trace();

    if request.method == 'GET':
        users = User.objects.all()
        content = []
        for user in users:
            info = {
                'name': user.first_name + ' ' + user.last_name,
                'email': user.email,
                'username': user.username,
                'user_id': user.id,
                'url': 'http://127.0.0.1:8001/accounts/' + str(user.id) + '/'
            }
            content.append(info)


        # content = json.dumps(users)
        # data = {'object_list': users}
        resp_content = json.dumps(content)
        return HttpResponse(resp_content)
    else:
        content = {'message': 'Invalid request'}
        error_message = json.dumps(content)
        return HttpResponse(error_message)