from rest_framework import serializers
from .models import Restaurant  # Asegúrate de que este import sea correcto

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant  
        fields = '__all__'  # Ajusta los campos si es necesario