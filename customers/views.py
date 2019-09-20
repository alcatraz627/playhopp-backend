from django.shortcuts import render
from rest_framework import viewsets, mixins, status, permissions, authentication
from rest_framework.decorators import action
# from rest_framework.views import APIView

from .models import Customer, HoppList, Subscription, Toy
from .serializers import CustomerSerializer, HoppListSerializer

# Create your views here.
class CustomerViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin
                        ):

    queryset=Customer.objects.all()
    serializer_class = CustomerSerializer

    lookup_field = 'email'

    # Enable using email addresses as lookup key
    # https://stackoverflow.com/questions/55714961/how-to-set-email-field-as-lookup-field-in-drf/55763166
    lookup_value_regex = '[^/]+'

    @action(detail=False, methods=['post'])
    def get_user(self, request):
        token = request.data['token']
        if 'token' in request.data:
            t = Token.objects.filter(key=token).first()
            return Response({'token': t.key,**CustomerSerializer(t.user).data}) if t is not None else Response("Token does not exist", status=status.HTTP_404_NOT_FOUND)

        return Response("Please specify token", status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        print(serializer.instance)
        # Sends same information as when logged in
        return Response({
            'token': token.key, 'email': serializer.instance.email, 'username': serializer.instance.email, 'first_name': serializer.instance.first_name,
            'address': serializer.instance.address, 'contact_number': serializer.instance.contact_number}, status=status.HTTP_201_CREATED)



class HoppListViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    queryset = HoppList.objects.all()
    serializer_class = HoppListSerializer

    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['PATCH'])
    def add(self, request, *args, **kwargs):
        h = HoppList.objects.get_or_create(customer=request.user, current=True)
        print(h)

        if ('toy' not in request.data):
            return Response("Please provide toy ID", status=status.HTTP_400_BAD_REQUEST)

        t = Toy.objects.filter(id=request.data['toy']).first()

        if t is not None:
            h.toys.add(t)
            return Response("Toy: [{}] added".format(t), status=status.HTTP_201_CREATED)
        else:
            return Response("Error: Toy not found", status=status.HTTP_404_NOT_FOUND)
        return Response("E")

    @action(detail=False, methods=['PATCH'])
    def remove(self, request, *args, **kwargs):
        if ('toy' not in request.data):
            return Response("Please provide toy ID", status=status.HTTP_400_BAD_REQUEST)

        h = self.get_object()
        t = Toy.objects.filter(id=request.data['toy'])
        print(h)
        print(t)
        print(h.toys)
        # print(t in h.toys)
        # if len(t) is not 0:
        #     t = t.first()
        #     if(t not in h.toys):
        #         return Response("DNE")
        #     else:
        #         return Response("YES")
        #     # h.toys.remove(t)
        #     # return Response("Toy: [{}] added".format(t), status=status.HTTP_201_CREATED)
        # else:
        #     return Response("Error: Toy not found", status=status.HTTP_404_NOT_FOUND)
        return Response("E")



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