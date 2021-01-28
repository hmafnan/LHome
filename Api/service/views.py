import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BookingSerializer
from .models import Booking


@api_view(['GET'])
def get_bookings(request):
    """Get all bookings"""
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_booking(request, email):
    """Get single"""
    booking = Booking.objects.get(email=email)
    serializer = BookingSerializer(booking, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_booking(request):
    """Create new booking
    Before creating the booking do validation checks
    """
    arrival_time = request.data.get('arrival_time').strip()
    departure_time = request.data.get('departure_time').strip()

    if arrival_time != '':
        request.data['arrival_time'] = datetime.datetime.strptime(arrival_time, '%Y-%m-%d(%H:%M:%S)')
    if departure_time != '':
        request.data['departure_time'] = datetime.datetime.strptime(departure_time, '%Y-%m-%d(%H:%M:%S)')

    serializer = BookingSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_booking(request, pk):
    """Delete booking"""
    booking = Booking.objects.get(id=pk)
    name = booking.name
    booking.delete()
    return Response('Booking deleted for %s' % name)

