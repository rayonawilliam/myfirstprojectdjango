from rest_framework import serializers
from .models import Advisor
from .models import bookadvisor
from .models import registeruser


from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

Usermodel=get_user_model()

class AdvisorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Advisor
        fields='__all__'

class userSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user =Usermodel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = Usermodel
        fields = ("id", "username", "password")





class bookappointment(serializers.ModelSerializer):

    class Meta:
        model=bookadvisor
        fields='__all__'

