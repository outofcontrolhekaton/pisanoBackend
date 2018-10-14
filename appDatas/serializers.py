from rest_framework import serializers
from .models import Pill, Pharmacy, Product


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'


class PillSerializer(serializers.ModelSerializer):
    pharmacies = PharmacySerializer(many=True, read_only=True)

    class Meta:
        model = Pill
        fields = ('title', 'image', 'QR_AI01', 'desc', 'pharmacies')


class ProductSerializer(serializers.ModelSerializer):
    pill = PillSerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ('pill', 'price', 'stock')


