from rest_framework import serializers

from .models import Customer, HoppList

class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)

    def create(self, validated_data):
        user = super(CustomerSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.email = user.username
        user.save()
        return user


    class Meta:
        model=Customer
        fields = ['username', 'password', 'first_name', 'last_name','address', 'contact_number']
        # fields = '__all__'


class HoppListSerializer(serializers.ModelSerializer):

    class Meta:
        model=HoppList
        fields = '__all__'
