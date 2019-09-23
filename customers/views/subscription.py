from rest_framework import viewsets, mixins, status, permissions, authentication
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Subscription, HoppList, Customer
from ..serializers import SubscriptionSerializer

class SubscriptionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    authentication_classes = [authentication.TokenAuthentication,authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request.data)

        serData = {**request.data, customer: request.user}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # @action(detail=False, methods=["GET"])
    # def current(self, request, *args, **kwargs):
    #     # s = HoppList.objects.filter(customer=request.user, current=True)
    #     # s = HoppList.objects.create(customer=request.user, current=True) if(h.count() == 0 ) else h.first()

    #     # return Response(HoppListSerializer(h).data)
