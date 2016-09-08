from rest_framework import serializers
from customers.models import Customers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('id',
                  'c_username',
                  'c_password',
                  'email',
                  'first_name',
                  'last_name')