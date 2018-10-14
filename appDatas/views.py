from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pill, Pharmacy, Product
from .serializers import PillSerializer, PharmacySerializer, ProductSerializer


# ------------------------------------- Pills -------------------------------------
class PillList(APIView):
    @staticmethod
    def get(request):
        pills = Pill.objects.all()
        serializer = PillSerializer(pills, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = PillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PillDetailById(APIView):
    @staticmethod
    def get_object_by_id(pk):
        try:
            return Pill.objects.get(pk=pk)
        except Pill.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pill = self.get_object_by_id(pk)
        serializer = PillSerializer(pill)
        return Response(serializer.data)

    def put(self, request, pk):
        pill = self.get_object_by_id(pk)
        serializer = PillSerializer(pill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pill = self.get_object_by_id(pk)
        pill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PillDetailByTitle(APIView):
    @staticmethod
    def get_object_by_title(title):
        try:
            return Pill.objects.get(title=title)
        except Pill.DoesNotExist:
            raise Http404

    def get(self, request, title):
        pill = self.get_object_by_title(title)
        serializer = PillSerializer(pill)
        return Response(serializer.data)

    def put(self, request, title):
        pill = self.get_object_by_title(title)
        serializer = PillSerializer(pill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, title):
        pill = self.get_object_by_title(title)
        pill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------------------- Products -------------------------------------
class ProductList(APIView):
    @staticmethod
    def get(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailById(APIView):
    @staticmethod
    def get_object_by_id(pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object_by_id(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object_by_id(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object_by_id(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductDetailByTitle(APIView):
    @staticmethod
    def get_object_by_title(title):
        try:
            return Product.objects.get(title=title)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, title):
        product = self.get_object_by_title(title)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, title):
        product = self.get_object_by_title(title)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, title):
        product = self.get_object_by_title(title)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------------------- Pharmacies -------------------------------------
class PharmacyList(APIView):
    @staticmethod
    def get(request):
        pharmacies = Pharmacy.objects.all()
        serializer = PharmacySerializer(pharmacies, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = PharmacySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PharmacyDetailById(APIView):
    @staticmethod
    def get_object_by_id(pk):
        try:
            return Pharmacy.objects.get(pk=pk)
        except Pharmacy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pharmacy = self.get_object_by_id(pk)
        serializer = PharmacySerializer(pharmacy)
        return Response(serializer.data)

    def put(self, request, pk):
        pharmacy = self.get_object_by_id(pk)
        serializer = PharmacySerializer(pharmacy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pharmacy = self.get_object_by_id(pk)
        pharmacy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PharmacyDetailByTitle(APIView):
    @staticmethod
    def get_object_by_title(title):
        try:
            return Pharmacy.objects.get(title=title)
        except Pharmacy.DoesNotExist:
            raise Http404

    def get(self, request, title):
        pharmacy = self.get_object_by_title(title)
        serializer = PillSerializer(pharmacy)
        return Response(serializer.data)

    def put(self, request, title):
        pharmacy = self.get_object_by_title(title)
        serializer = PillSerializer(pharmacy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, title):
        pharmacy = self.get_object_by_title(title)
        pharmacy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
