# from django.conf import settings
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status, permissions, authentication
from rest_framework.decorators import action
from backend.helpers import get_image_url

from ..models import HoppList, Toy
from ..serializers import HoppListSerializer

class HoppListViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    queryset = HoppList.objects.all()
    serializer_class = HoppListSerializer

    authentication_classes = [authentication.TokenAuthentication,authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["GET"])
    def current(self, request, *args, **kwargs):
        h = HoppList.objects.filter(customer=request.user, current=True)
        h = HoppList.objects.create(customer=request.user, current=True) if(h.count() == 0 ) else h.first()

        return Response(HoppListSerializer(h).data)

    @action(detail=False, methods=["DELETE"])
    def empty(self, request, *args, **kwargs):
        h = HoppList.objects.get_or_create(customer=request.user, current=True)[0]
        h.toys.clear()
        return Response("Hopplist for user {} cleared".format(request.user.first_name), status=status.HTTP_204_NO_CONTENT)


    @action(detail=False, methods=["POST"])
    def add(self, request, *args, **kwargs):
        if "toy" not in request.data:
            return Response("Please provide toy ID", status=status.HTTP_400_BAD_REQUEST)

        h = HoppList.objects.get_or_create(customer=request.user, current=True)[0]
        t = Toy.objects.filter(id=request.data["toy"]).first()

        if t is not None:
            h.toys.add(t)
            return Response("Toy: [{}] added".format(t), status=status.HTTP_200_OK)
        else:
            return Response("Error: Toy not found", status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["POST"])
    def remove(self, request, *args, **kwargs):
        if "toy" not in request.data:
            return Response("Please provide toy ID", status=status.HTTP_400_BAD_REQUEST)

        h = HoppList.objects.get_or_create(customer=request.user, current=True)[0]
        t = Toy.objects.filter(id=request.data["toy"]).first()

        if t is not None:
            h.toys.remove(t)
            return Response("Toy: [{}] removed".format(t), status=status.HTTP_200_OK)
        else:
            return Response("Error: Toy not found", status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["POST"])
    def remove(self, request, *args, **kwargs):
        if "toy" not in request.data:
            return Response("Please provide toy ID", status=status.HTTP_400_BAD_REQUEST)

        h = HoppList.objects.get_or_create(customer=request.user, current=True)[0]
        t = Toy.objects.filter(id=request.data["toy"]).first()

        if t is not None:
            h.toys.remove(t)
            return Response("Toy: [{}] removed".format(t), status=status.HTTP_200_OK)
        else:
            return Response("Error: Toy not found", status=status.HTTP_404_NOT_FOUND)
