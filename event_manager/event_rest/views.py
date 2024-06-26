from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'date', 'location']

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class EventRegistrationCreate(generics.CreateAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        event_registration = serializer.save(user=self.request.user)
        send_mail(
            'Event Registration Confirmation',
            f'You have successfully registered for the event: {event_registration.event.title}',
            'from@example.com',
            [self.request.user.email],
            fail_silently=False,
        )


