from django.urls import path
from .views import (HomepageView, AboutpageView, ContactpageView, ServicespageView,
                    EventListView, EventDetailView, EventCreateView,
                    EventUpdateView, EventDeleteView)

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('blog/', ServicespageView.as_view(), name='blog'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('contact/', ContactpageView.as_view(), name='contact'),
    path('services/', EventListView.as_view(), name='services'),
    path('event/<int:pk>', EventDetailView.as_view(), name='event_detail'),
    path('event/create', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/edit', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name='event_delete'),
]