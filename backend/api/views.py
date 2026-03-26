from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import RepairRequest
from .serializers import RepairRequestSerializer


# 🔥 SUBMIT REQUEST (AUTO ASSIGN MECHANIC)
@api_view(['POST'])
def submit_request(request):
    serializer = RepairRequestSerializer(data=request.data)

    if serializer.is_valid():
        obj = serializer.save()

        # ✅ AUTO ASSIGN MECHANIC
        mechanic = User.objects.filter(username__startswith='mechanic').first()

        if mechanic:
            obj.mechanic = mechanic

        obj.status = 'Accepted'
        obj.save()

        return Response({
            'id': obj.id,
            'status': obj.status,
            'mechanic': obj.mechanic.username if obj.mechanic else None
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 🔥 GET SINGLE REQUEST (TRACK PAGE)
@api_view(['GET'])
def get_request(request, pk):
    try:
        req = RepairRequest.objects.get(pk=pk)

        return Response({
            'id': req.id,
            'status': req.status,
            'mechanic': req.mechanic.username if req.mechanic else None,
            'vehicle': req.vehicle,
            'problem': req.problem,
            'timestamp': req.timestamp
        })

    except RepairRequest.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


# 🔥 GET ALL REQUESTS (DASHBOARD)
@api_view(['GET'])
def get_all_requests(request):
    reqs = RepairRequest.objects.all().order_by('-timestamp')
    return Response(RepairRequestSerializer(reqs, many=True).data)


# 🔐 LOGIN
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return Response({'success': True, 'username': user.username})

    return Response({'success': False}, status=status.HTTP_401_UNAUTHORIZED)


# 🔐 LOGOUT
@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({'success': True})