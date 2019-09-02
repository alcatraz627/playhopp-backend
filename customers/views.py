from django.shortcuts import render
from rest_framework import viewsets

from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):

    queryset=Customer.objects.all()
    serializer_class = CustomerSerializer

    lookup_field = 'email'

    # https://stackoverflow.com/questions/55714961/how-to-set-email-field-as-lookup-field-in-drf/55763166
    lookup_value_regex = '[^/]+'


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'email': user.email,
            'first_name': user.first_name,
            'contact_number': user.contact_number,
        })