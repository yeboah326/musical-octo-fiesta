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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default="unknownDoctor") # remove default in main project
    hospital = models.ForeignKey(Hospital,related_name="doctors",on_delete=models.CASCADE)
    profilePicture = models.ImageField(upload_to='profiles/DoctorProfilePictures',default='profiles/DoctorProfilePictures/dummy_profile.png')
    numberOfReportsAssigned = models.PositiveIntegerField(default=0)
    numberOfReportsCompleted = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = ('doctor')
        verbose_name_plural = ('doctors')

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"

    def get_absolute_url(self):
        return reverse("nurse_detail", kwargs={"pk": self.pk})

class Nurse(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default="unknownNurse") # remove default in main project
    hospital = models.ForeignKey(Hospital, related_name="nurses", on_delete=models.CASCADE)
    profilePicture = models.ImageField(upload_to='profiles/NurseProfilePictures',default='profiles/DoctorProfilePictures/dummy_profile.png')
    numberOfReportsCreated = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = ("nurse")
        verbose_name_plural = ("nurses")

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"

    def get_absolute_url(self):
        return reverse("nurse_detail", kwargs={"pk": self.pk})
