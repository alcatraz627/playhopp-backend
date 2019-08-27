from rest_framework import serializers

from .models import Category, Brand, Toy


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'
