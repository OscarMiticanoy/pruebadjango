from rest_framework import serializers
from django.contrib.auth.models import User

class Users(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    email = serializers.EmailField()
    fechaNacimiento = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    password = serializers.CharField()

    def create(self, data):
        instance = User()
        instance.nombres = data.get('nombres')
        instance.apellidos = data.get('apellidos')
        instance.email = data.get('email')
        instance.fechaNacimiento = data.get('fechaNacimiento')
        instance.set_password(data.get('password'))
        instance.save()
        return instance

    def validateUserName(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            return True
        else:
            return False
    
    
