from rest_framework import serializers
from .models import TableProduct

class PruductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableProduct
        fields = '__all__'