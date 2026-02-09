
from django.db import models

import uuid

class Doctor(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=255)
    Specialization = models.CharField(max_length=255)
    Phone_Number = models.BigIntegerField()


    class Meta:
        db_table = 'doctor' 

    def __str__(self):
        return f"Doctor: {self.Name}"
    


class Slot(models.Model):
    Slot_Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Start_time = models.TimeField()
    End_time = models.TimeField()

    class Meta:
        db_table = 'slot' 

    def __str__(self):
        return f"Slot {self.Id} ({self.Start_time} - {self.End_time})"
    

class Patient(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=255)
    Age = models.PositiveIntegerField()

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    Concerns = models.TextField()
    Phone_Number = models.BigIntegerField()

    class Meta:
        db_table = 'patient'  

    def __str__(self):
        return f"Patient: {self.Name}"

class Bookings(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Patient_Id =  models.ForeignKey(
        Patient,
        to_field='Id',
        on_delete=models.CASCADE,
        
    )
    Doctor_Id = models.ForeignKey(
        Doctor,
        to_field='Id',
        on_delete=models.CASCADE,
        
    )
    Slot_Id = models.ForeignKey(
        Slot,
        to_field='Slot_Id',
        on_delete=models.CASCADE,
        
    )
    Date = models.DateField()
    is_booked = models.BooleanField(default= True)

    class Meta:
        db_table = 'bookings'
