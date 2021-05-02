from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Hospital(models.Model):

    name = models.CharField(max_length=100, help_text="Enter the name of the hospital")

    class Meta:
        verbose_name = ("hospital")
        verbose_name_plural = ("hospitals")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hospital_detail", kwargs={"pk": self.pk})

class Doctor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="doctors")
    name = models.CharField(max_length=50,default="unknownDoctor") # remove default in main project
    hospital = models.ForeignKey(Hospital,related_name="doctors",on_delete=models.CASCADE)
    profilePicture = models.ImageField(upload_to='profiles/DoctorProfilePictures',default='profiles/DoctorProfilePictures/dummy_profile.png')
    numberOfReportsAssigned = models.PositiveIntegerField(default=0) # Make these field non-editable in main project
    numberOfReportsCompleted = models.PositiveIntegerField(default=0) # Make these field non-editable in main project


    class Meta:
        verbose_name = ('doctor')
        verbose_name_plural = ('doctors')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("nurse_detail", kwargs={"pk": self.pk})

class Nurse(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="nurses")
    name = models.CharField(max_length=50,default="unknownNurse") # remove default in main project
    hospital = models.ForeignKey(Hospital, related_name="nurses", on_delete=models.CASCADE)
    profilePicture = models.ImageField(upload_to='profiles/NurseProfilePictures',default='profiles/DoctorProfilePictures/dummy_profile.png')
    numberOfReportsCreated = models.PositiveIntegerField(default=0) # Make these field non-editable in main project

    class Meta:
        verbose_name = ("nurse")
        verbose_name_plural = ("nurses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("nurse_detail", kwargs={"pk": self.pk})

class Report(models.Model):
    STATUS = (
        ("done", "DONE"),
        ("pending", "PENDING"),
    )

    name = models.CharField(max_length=100) # Will be changed to an auto-generated one
    reportImage = models.ImageField()
    doctor = models.ForeignKey(Doctor,related_name="assigned_reports",on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, related_name="generated_reports", on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, related_name="reports", on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now=True)
    completedOn = models.DateTimeField()
    message = models.TextField()
    comments = models.TextField(null=True,blank=True)
    completed = models.CharField(choices=STATUS,max_length=8)

    # Will return to this
    @property
    def url(self):
        return self.name.replace(" ", "_").lower()
    
    class Meta:
        verbose_name = ("report")
        verbose_name_plural = ("reports")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("report_detail", kwargs={"pk": self.pk})
