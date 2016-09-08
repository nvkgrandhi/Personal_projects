from rest_framework import serializers
from products.models import Category, SubCategory


class ProductSerializer(serializers.ModelSerializer):
    subcategory = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'subcategory')