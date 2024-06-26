from django.urls import include, path
from rest_framework.routers import DefaultRouter

from event_rest.views import EventViewSet, EventRegistrationCreate

router = DefaultRouter()
router.register('event_rest', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', EventRegistrationCreate.as_view()),
]