from tkinter import Entry
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from entries.models import EntryModel

from entries.api.serializers import EntrySerializer

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
    
class EntryListAPI(APIView):
    def get(self, resquest, pk):
        
        entries = EntryModel.objects.all()
        
        serializer = EntrySerializer(entries, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, pk):
        
        serializer = EntrySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        
        return Response(status=400, data=serializer.errors)
    
    def put(self, request, pk):
        
        entry = get_object_or_404(EntryModel, pk=pk)
        
        
        serializer = EntrySerializer(instance=entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    def delete(self, request, pk):
        
        entry = get_object_or_404(EntryModel, pk=pk)
       
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
