from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User
from .serializers import UserSerializer  # Ensure you import the correct serializer

@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        # Get all users
        users = User.objects.all()

        # Serialize the data and return as response
        serializer = UserSerializer(users, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def users_detail(request, id):
    try:
        # Retrieve the user by id
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        # Update the user data
        serializer = UserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
