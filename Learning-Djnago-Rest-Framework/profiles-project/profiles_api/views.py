from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers



class helloAPIView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        an_apiview = [
            'yo',
            'hi',
            'hello',
            'hola',
            'howdy',
        ]

        return Response({'message': 'Good Morning', 'an_apiView' : an_apiview})
    
    def post(self, request):
        
        seriaizer = self.serializer_class(data=request.data)

        if seriaizer.is_valid():
            name = seriaizer.validated_data.get('name')
            return Response({'sent string': name})
        
        return Response(seriaizer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def put(self, request, pk = None):
        return Response({'method' : 'PUT'}) 
        
        
    def patch(self, request, pk = None):
        return Response({'method' : 'PATCH'}) 
    
    def delete(self, request, pk = None):
        return Response({'method' : 'DELETE'}) 
    


