from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User, Event, VolunteerRegistration, EnvironmentalResource, ImpactReport, Recognition, Admin
from django.urls import reverse_lazy

class HomepageView(TemplateView):
    template_name = 'app/home.html'


class ServicespageView(TemplateView):
    template_name = 'app/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = None
        volunteerregistration = None

        # Check if the user is logged in
        if 'user_id' in self.request.session:
            try:
                user = User.objects.get(id=self.request.session['user_id'])
                volunteerregistration = VolunteerRegistration.objects.filter(user=user)  # Get health goals for the user
            except User.DoesNotExist:
                messages.error(self.request, "User not found.")

        # Pass all data objects for display in tables
        context['user'] = user
        context['volunteerregistration'] = volunteerregistration
        context['event'] = Event.objects.all()
        context['environmentalresource'] = EnvironmentalResource.objects.all()
        context['impactreport'] = ImpactReport.objects.all()
        context['recognition'] = Recognition.objects.all()

        # Pass the counts for each table
        context['user_count'] = User.objects.count()
        context['event'] = Event.objects.count()
        context['volunteerregistration_count'] = VolunteerRegistration.objects.count()
        context['environmentalresource_count'] = EnvironmentalResource.objects.count()
        context['impactreport_count'] = ImpactReport.objects.count()
        context['recognition_count'] = Recognition.objects.count()

        return context


class AboutpageView(TemplateView):
    template_name = 'app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = None
        volunteerregistration = None

        # Check if the user is logged in
        if 'user_id' in self.request.session:
            try:
                user = User.objects.get(id=self.request.session['user_id'])
                volunteerregistration = VolunteerRegistration.objects.filter(user=user)  # Get health goals for the user
            except User.DoesNotExist:
                messages.error(self.request, "User not found.")

        # Pass all data objects for display in tables
        context['user'] = user
        context['volunteerregistration'] = volunteerregistration
        context['event'] = Event.objects.all()
        context['environmentalresource'] = EnvironmentalResource.objects.all()
        context['impactreport'] = ImpactReport.objects.all()
        context['recognition'] = Recognition.objects.all()

        # Pass the counts for each table
        context['user_count'] = User.objects.count()
        context['event'] = Event.objects.count()
        context['volunteerregistration_count'] = VolunteerRegistration.objects.count()
        context['environmentalresource_count'] = EnvironmentalResource.objects.count()
        context['impactreport_count'] = ImpactReport.objects.count()
        context['recognition_count'] = Recognition.objects.count()

        return context

class ContactpageView(TemplateView):
    template_name = 'app/contact.html'


class EventListView(ListView):
    model = Event
    context_object_name = 'Event'
    template_name = 'app/event_list.html'


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'Events'
    template_name = 'app/event_detail.html'


class EventCreateView(CreateView):
    model = Event
    fields = ['title', 'description', 'location', 'event_date', 'start_time', 'end_time',
               'max_volunteers']
    template_name = 'app/event_create.html'

class EventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'description', 'location', 'event_date', 'start_time', 'end_time',
             'max_volunteers']
    template_name = 'app/event_update.html'

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'app/event_delete.html'
    success_url = reverse_lazy('services')

class DatabasePageView(TemplateView):
    template_name = 'app/database.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Pass all data objects for display in tables
        context['user'] = User.objects.all()
        context['event'] = Event.objects.all()
        context['volunteerregistration'] = VolunteerRegistration.objects.all()
        context['environmentalresource'] = EnvironmentalResource.objects.all()
        context['impactreport'] = ImpactReport.objects.all()
        context['recognition'] = Recognition.objects.all()

        # Pass the counts for each table
        context['user_count'] = User.objects.count()
        context['event_count'] = Event.objects.count()
        context['volunteerregistration_count'] = VolunteerRegistration.objects.count()
        context['environmentalresource_count'] = EnvironmentalResource.objects.count()
        context['impactreport_count'] = ImpactReport.objects.count()
        context['recognition_count'] = Recognition.objects.count()

        return context

    @staticmethod
    def admin_dashboard(request):
        # Calculate the counts
        user_count = User.objects.count()
        event_count = Event.objects.count()
        volunteerregistration_count = VolunteerRegistration.objects.count()
        environmentalresource_count = EnvironmentalResource.objects.count()
        impactreport_count = ImpactReport.objects.count()
        recognition_count = Recognition.objects.count()

        return render(request, 'app/admin_dashboard.html', {
            'user_count': user_count,
            'event_count': event_count,
            'volunteerregistration_count': volunteerregistration_count,
            'environmentalresource_count': environmentalresource_count,
            'impactreport_count': impactreport_count,
            'recognition_count': recognition_count,

        })

class AdminUserCreateView(CreateView):
    model = User
    fields = ['name', 'email', 'password']
    template_name = 'app/add_user.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'


class AdminEventCreateView(CreateView):
    model = Event
    fields = ['title', 'description', 'location', 'event_date',
             'start_time', 'end_time', 'max_volunteers']
    template_name = 'app/add_event.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminVolunteerRegistrationCreateView(CreateView):
    model = VolunteerRegistration
    fields = ['event', 'user', 'task_assigned']
    template_name = 'app/add_volunteerregistration.html'

    def get_success_url(self):
        return reverse_lazy('blog') + '?section=users'

class AdminEnvironmentalResourceCreateView(CreateView):
    model = EnvironmentalResource
    fields = ['title', 'content', 'resource_type']
    template_name = 'app/add_environmentalresource.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminImpactReportCreateView(CreateView):
    model = ImpactReport
    fields = ['event', 'waste_collected_kg', 'participant_testimonials']
    template_name = 'app/add_impactreport.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminRecognitionCreateView(CreateView):
    model = Recognition
    fields = ['user', 'event', 'recognition_text']
    template_name = 'app/add_recognition.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminUserUpdateView(UpdateView):
    model = User
    fields = ['name', 'email', 'password']
    template_name = 'app/update_user.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminEventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'description', 'location', 'event_date',
              'start_time', 'end_time', 'max_volunteers']
    template_name = 'app/update_event.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminVolunteerRegistrationUpdateView(UpdateView):
    model = VolunteerRegistration
    fields = ['event', 'user', 'task_assigned']
    template_name = 'app/update_volunteerregistration.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminEnvironmentalResourceUpdateView(UpdateView):
    model = EnvironmentalResource
    fields = ['title', 'content', 'resource_type']
    template_name = 'app/update_environment.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminImpactReportUpdateView(UpdateView):
    model = ImpactReport
    fields = ['event', 'waste_collected_kg', 'participant_testimonials']
    template_name = 'app/update_impactreport.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminRecognitionUpdateView(UpdateView):
    model = Recognition
    fields = ['user', 'event', 'recognition_text']
    template_name = 'app/update_recognition.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminUserDeleteView(DeleteView):
    model = User
    fields = ['name', 'email', 'password']
    template_name = 'app/delete_user.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminEventDeleteView(DeleteView):
    model = Event
    fields = ['title', 'description', 'location', 'event_date',
              'start_time', 'end_time', 'max_volunteers']
    template_name = 'app/delete_event.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminVolunteerRegistrationDeleteView(DeleteView):
    model = VolunteerRegistration
    fields = ['event', 'user', 'task_assigned']
    template_name = 'app/delete_volunteerregistration.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminEnvironmentalResourceDeleteView(DeleteView):
    model = EnvironmentalResource
    fields = ['title', 'content', 'resource_type']
    template_name = 'app/delete_environment.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminImpactReportDeleteView(DeleteView):
    model = ImpactReport
    fields = ['event', 'waste_collected_kg', 'participant_testimonials']
    template_name = 'app/delete_impactreport.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminRecognitionDeleteView(DeleteView):
    model = Recognition
    fields = ['user', 'event', 'recognition_text']
    template_name = 'app/delete_recognition.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class LoginFormTemplateView(TemplateView):
    template_name = 'registration/login.html'


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if the user exists in the database
            admin = Admin.objects.get(username=username)
            if admin.password == password:
                # Login successful
                request.session['admin_id'] = admin.id
                request.session['admin_firstname'] = admin.firstname
                messages.success(request, "Admin login successful")
                return redirect('database')
            else:
                # Invalid password message
                messages.error(request, "Invalid username or password.")
        except Admin.DoesNotExist:  # Handle Admin-specific DoesNotExist
            messages.error(request, "Admin does not exist. Please contact support.")

    # Render login page even if there are errors
    return render(request, 'registration/admin_login.html')


def customer_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            # Check if the user exists in the database
            user = User.objects.get(name=name)
            if user.password == password:
                # Save user ID in session for login state
                request.session['user_id'] = user.id
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, "Invalid username or password.")  # Invalid password message
        except User.DoesNotExist:
            messages.error(request, "Customer does not exist. Please register first.")  # User not found message

    # Render login page even if there are errors
    return render(request, 'registration/login.html')

def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')



        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('customer_login')

        user = User(
            name=name,
            email=email,
            password=password,
        )
        user.save()
        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'registration/register.html')