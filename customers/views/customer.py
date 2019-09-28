from rest_framework.response import Response
# from django.conf import settings
from rest_framework import viewsets, mixins, status, permissions, authentication
from rest_framework.decorators import action

from rest_framework.authtoken.models import Token
from ..models import Customer
from ..serializers import CustomerSerializer

from backend.helpers import get_image_url

# Create your views here.
class CustomerViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                ):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    lookup_field = "email"

    # Enable using email addresses as lookup key
    # https://stackoverflow.com/questions/55714961/how-to-set-email-field-as-lookup-field-in-drf/55763166
    lookup_value_regex = "[^/]+"

    @action(detail=False, methods=["post"])
    def get_user(self, request):
        if "token" in request.data:
            token = request.data["token"]
            t = Token.objects.filter(key=token).first()

            return (
                Response({"token": t.key, **CustomerSerializer(t.user).data, "profile_pic": get_image_url(t.user.profile_pic, request)})
                if t is not None
                else Response("Token does not exist", status=status.HTTP_404_NOT_FOUND)
            )

        return Response("Please specify token", status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        print(serializer.instance)

        # TODO: Set a default avatar as profile pic
        return Response(
            {
                "token": token.key,
                "email": serializer.instance.email,
                "username": serializer.instance.email,
                "first_name": serializer.instance.first_name,
                "address": serializer.instance.address,
                "contact_number": serializer.instance.contact_number,
            },
            status=status.HTTP_201_CREATED,
        )
