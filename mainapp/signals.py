from random import choice

from django.dispatch import receiver
from django.db.models.signals import post_save

from mainapp.models import Doctor, Nurse


@receiver(post_save, sender=Doctor)
def add_doctor_to_nurse(sender, instance, created, **kwargs):

    if created:

        Nurse.objects.filter(
            pk=choice(
                range(1,Nurse.objects.count()+1) #Assign random nurse to a created doctor
            )
        ).update(doctor=instance.id)
        print('Nurse added to created doctor!')
