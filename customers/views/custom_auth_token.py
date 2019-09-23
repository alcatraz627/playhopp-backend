from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from backend.helpers import get_image_url


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "email": user.email,
                "username": user.email,
                "first_name": user.first_name,
                "address": user.address,
                "contact_number": user.contact_number,
                "profile_pic": get_image_url(user.profile_pic, request),
            }
        )
