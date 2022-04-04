from django.db import models


# Create your models here.
class Class(models.Model):
    floor = models.IntegerField()
    door = models.CharField(max_length=1)

    def __str__(self):
        return str(self.floor) + ' - ' + self.door

    class Meta:
        verbose_name_plural = 'Classes'


class Student(models.Model):
    name = models.CharField(max_length=20)

    own_class = models.ForeignKey(
        Class,
        related_name='students',
        verbose_name='Class to which this student belongs',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name + ', ' + str(self.own_class.floor) + '-' + self.own_class.door

    class Meta:
        verbose_name_plural = 'Students'
