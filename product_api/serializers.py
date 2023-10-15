from rest_framework import serializers
from .models import Product
from django.forms import ValidationError


class ProductSerializer(serializers.ModelSerializer):
    subDescription = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'price', 'quantity', 'description', 'subDescription'
        )

    # 驗證某一個屬性的值不可為什麼值
    def validate_name(self, value):
        if value == 'admin':
            raise ValidationError("admin 禁止使用")
        return value

    # 限制屬性值得範圍
    def validate(self, data):
        if data['price'] > 10000 or data['quantity'] > 10:
            raise ValidationError("金額或數量超過限制")
        return data
        
    # 新增附加描述的字段
    def get_subDescription(self, data):
        return f"產品名稱:{data.name}, 價格:${str(data.price)}, 數量:{str(data.quantity)}"


    # 一般序列化寫法
    # class ProductSerializer(serializers.Serializer):
    #   id = serializers.IntegerField(read_only=True)
    #   name = serializers.CharField()
    #   price = serializers.IntegerField()
    #   quantity = serializers.IntegerField()
    #   quantity = serializers.CharField()

    # 建立資料
    # def create(self, data):
        # return Product.objects.create(**data)
    
    # 更新資料
    # def update(self, instance, data):
    #   instance.name = data.get('name', instance.name)  
    #   instance.price = data.get('price', instance.price)  
    #   instance.quantity = data.get('quantity', instance.quantity)  
    #   instance.description = data.get('description', instance.description)  

    #   instance.save()
    #   return instance

