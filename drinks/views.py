from django.http import JsonResponse, HttpResponse
from .models import drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore


def hoempage(request):
    return HttpResponse("Welcome to HomePage!")

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        #get all the drinks, serialize them & return json
        drinks = drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({"drinks": serializer.data})

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # type: ignore
        
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):  
    try:      
        drinks = drink.objects.get(pk=id)
    except drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drinks)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drinks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        drinks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    