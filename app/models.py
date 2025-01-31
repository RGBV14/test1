from django.db import models
from django.urls import reverse


class Admin(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length =300)
    location = models.CharField(max_length=255)
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_volunteers = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})


class VolunteerRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    task_assigned = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} registered for {self.event.title}"


class EnvironmentalResource(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    resource_type = models.CharField(max_length=50, choices=[('safety', 'Safety'), ('cleanup', 'Cleanup Tips'), ('environmental', 'Environmental Best Practices')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ImpactReport(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="impact_reports")
    waste_collected_kg = models.DecimalField(max_digits=6, decimal_places=2)
    participant_testimonials = models.TextField()
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Impact Report for {self.event.title}"


class Recognition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recognitions")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    recognition_text = models.TextField(help_text="Reason for recognition, e.g., standout volunteer")
    date_awarded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recognition for {self.user.name} in {self.event.title}"