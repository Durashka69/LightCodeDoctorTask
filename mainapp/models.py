from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Doctor(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='doctor',
        verbose_name='Пользователь'
    )
    job_title = models.CharField(default='Врач', max_length=255)

    def __str__(self):
        return f'{self.job_title} - {self.user.username}'

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"


class Nurse(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='nurse',
        verbose_name='Пользователь'
    )
    job_title = models.CharField(default='Медсестра', max_length=255)
    doctor = models.ForeignKey(
        Doctor, 
        on_delete=models.PROTECT,
        null=True, blank=True,
        related_name='nurse',
        verbose_name='врач'  
    )

    def __str__(self):
        return f'{self.job_title} - {self.user.username}'

    class Meta:
        verbose_name = "Медсестра"
        verbose_name_plural = "Медсёстры"
