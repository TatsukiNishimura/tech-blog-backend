from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenAndExpireDateSerialiser(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['expires_at'] = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
        return data
