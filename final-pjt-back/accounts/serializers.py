from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = get_user_model()
        fields = '__all__' # 수정 필요
