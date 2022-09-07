from random import choice

from django.dispatch import receiver
from django.db.models.signals import post_save

from mainapp.models import Doctor, Nurse


def except_id(num, end, start = 1):   #this function gives us list of nums except one value that we will choose
    return [i for i in range(start, num)] + [j for j in range(num+1, end)] #soon it will be needed if id of nurse's user will
                                                                           # be the same as doctor's user's id.


@receiver(post_save, sender=Doctor)
def add_doctor_to_nurse(sender, instance, created, **kwargs):

    print(f'\n\n\n\n\n\n\n\n{instance.id} is instance.id \n\n\n\n\n\n ')

    if created:

        free_nurses = Nurse.objects.filter(doctor=None) #Takes all nurses which doesn't have a doctor
        nurse = free_nurses.first()

        if nurse.user.id == instance.user.id: #checks if doctor is not a nurse (because doctors also can be nurses)
            nurse_choice = choice(            #so i decided that doctor can't be his own nurse lol
                except_id(nurse.id, len(free_nurses))
            )
            nurse = free_nurses[nurse_choice]

        nurse.doctor = instance
        nurse.save()
        print('free_nurses added to created doctor!')
