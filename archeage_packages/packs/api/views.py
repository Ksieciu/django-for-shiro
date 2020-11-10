from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Pack, Component
from .serializers import ComponentSerializer, PackSerializer


class PackList(generics.ListAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer


class PackDetails(generics.RetrieveAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer


@api_view(['POST'])
def add_pack_view(request, *args, **kwargs):
    serializer = PackSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Record created/updated", status=201)
    return Response({}, status=400)