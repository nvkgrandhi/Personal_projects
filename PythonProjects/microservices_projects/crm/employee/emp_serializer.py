from rest_framework import serializers
from employee.models import Employees, Departments


class EmpDeptSerializer(serializers.ModelSerializer):
    department = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'gender', 'department')
