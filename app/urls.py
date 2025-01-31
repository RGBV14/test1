from django.urls import path
from .import views
from .views import (HomepageView, AboutpageView, ContactpageView, ServicespageView,
                    EventListView, EventDetailView, EventCreateView,
                    EventUpdateView, EventDeleteView, DatabasePageView, AdminUserCreateView,
                    AdminEventCreateView, AdminVolunteerRegistrationCreateView, AdminEnvironmentalResourceCreateView,
                    AdminImpactReportCreateView, AdminRecognitionCreateView, AdminUserUpdateView,
                    AdminEventUpdateView, AdminVolunteerRegistrationUpdateView, AdminEnvironmentalResourceUpdateView,
                    AdminImpactReportUpdateView, AdminRecognitionUpdateView, AdminUserDeleteView, AdminEventDeleteView,
                    AdminVolunteerRegistrationDeleteView, AdminEnvironmentalResourceDeleteView,
                    AdminImpactReportDeleteView, AdminRecognitionDeleteView, LoginFormTemplateView)

urlpatterns = [

    path('', LoginFormTemplateView.as_view(), name='login'),
    path('customer-login/', views.customer_login, name='customer_login'),
    path('admin_login/', views.admin_login, name='login_admin'),
    path('register_user/', views.register_user, name='register_user'),

    path('home/', HomepageView.as_view(), name='home'),
    path('blog/', ServicespageView.as_view(), name='blog'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('contact/', ContactpageView.as_view(), name='contact'),
    path('services/', EventListView.as_view(), name='services'),
    path('event/<int:pk>', EventDetailView.as_view(), name='event_detail'),
    path('event/create', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/edit', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name='event_delete'),

    path('database/', DatabasePageView.as_view(), name='database'),

    path('adduser/create', AdminUserCreateView.as_view(), name='add_user'),
    path('updateuser/<int:pk>/edit', AdminUserUpdateView.as_view(), name='update_user'),
    path('deleteuser/<int:pk>/delete', AdminUserDeleteView.as_view(), name='delete_user'),

    path('addevent/create', AdminEventCreateView.as_view(), name='add_event'),
    path('updateevent/<int:pk>/edit', AdminEventUpdateView.as_view(), name='update_event'),
    path('deleteevent/<int:pk>/delete', AdminEventDeleteView.as_view(), name='delete_event'),

    path('addvolunteerregistration/create', AdminVolunteerRegistrationCreateView.as_view(), name='add_volunteerregistration'),
    path('updatevolunteerregistration/<int:pk>/edit', AdminVolunteerRegistrationUpdateView.as_view(), name='update_volunteerregistration'),
    path('deletevolunteerregistration/<int:pk>/delete', AdminVolunteerRegistrationDeleteView.as_view(), name='delete_volunteerregistration'),

    path('addenvironmentalresource/create', AdminEnvironmentalResourceCreateView.as_view(), name='add_environmentalresource'),
    path('updateenvironment/<int:pk>/edit', AdminEnvironmentalResourceUpdateView.as_view(), name='update_environment'),
    path('deleteenvironment/<int:pk>/delete', AdminEnvironmentalResourceDeleteView.as_view(), name='delete_environment'),

    path('addimpactreport/create', AdminImpactReportCreateView.as_view(), name='add_impactreport'),
    path('updateimpactreport/<int:pk>/edit', AdminImpactReportUpdateView.as_view(), name='update_impactreport'),
    path('deleteimpactreport/<int:pk>/delete', AdminImpactReportDeleteView.as_view(),  name='delete_impactreport'),

    path('addrecognition/create', AdminRecognitionCreateView.as_view(), name='add_recognition'),
    path('updaterecognition/<int:pk>/edit', AdminRecognitionUpdateView.as_view(), name='update_recognition'),
    path('deleterecognition/<int:pk>/delete', AdminRecognitionDeleteView.as_view(), name='delete_recognition'),

]