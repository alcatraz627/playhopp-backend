from rest_framework import serializers

from .models import Customer, HoppList, Subscription

class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, write_only=True)

    def create(self, validated_data):
        user = super(CustomerSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.email = user.username
        user.save()
        return user

    def update(self, instance, validated_data):
        super(CustomerSerializer, self).update(instance, validated_data)
        if 'password' in validated_data: instance.set_password(validated_data['password'])
        if 'username' in validated_data: instance.email = validated_data['username']
        instance.save()
        return instance


    class Meta:
        model=Customer
        fields = ['username', 'password', 'first_name', 'last_name','address', 'contact_number', 'profile_pic']
        # fields = '__all__'


class HoppListSerializer(serializers.ModelSerializer):

    class Meta:
        model=HoppList
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    hopplist = serializers.SerializerMethodField()

    def get_hopplist(self, obj):
        return obj.hopplist.id
        # return HoppListSerializer(obj.hopplist).data

    class Meta:
        model=Subscription
        fields = ['id', 'hopplist', 'customer', 'address', 'contact_number', 'email']
