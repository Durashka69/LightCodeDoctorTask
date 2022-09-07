from random import choice

from mainapp.models import Nurse


nurse = Nurse.objects.filter(
    pk=choice(
        range(
            Nurse.objects.count()
        )
    )
).first()

print(nurse)
