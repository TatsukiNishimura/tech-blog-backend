from rest_framework_simplejwt.views import TokenObtainPairView

from blog.auth.serializer import TokenAndExpireDateSerialiser


class TokenObtainPairWithExpiredDateView(TokenObtainPairView):
    serializer_class = TokenAndExpireDateSerialiser
