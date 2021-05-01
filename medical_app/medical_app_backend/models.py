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
    hospital = models.ForeignKey(Hospital,related_name="doctors",on_delete=models.CASCADE)
    profilePicture = models.ImageField(upload_to='profiles/DoctorProfilePictures',default='profiles/DoctorProfilePictures/dummy')
    numberOfReportsAssigned = models.IntegerField(default=0)
    numberOfReportsCompleted = models.IntegerField(default=0)


    class Meta:
        verbose_name = ('doctor')
        verbose_name_plural = ('doctors')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("nurse_detail", kwargs={"pk": self.pk})

