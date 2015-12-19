from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.CharField(max_length=30)
    pw = models.CharField(max_length=16)
    name = models.CharField(max_length=50, blank=True)

    NOT_SET = 'NOT'
    MALE = 'MAL'
    FEMALE = 'FEM'
    THIRD = 'THD'
    GENDER_CHOICES = (
        (NOT_SET, 'Not Set'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (THIRD, 'The 3rd'),
    )
    gender = models.CharField(max_length=3,
                           choices=GENDER_CHOICES,
                           default=NOT_SET)

    TEENS = 'TNS'
    TWENTIES = 'TWT'
    THIRTIES = 'THT'
    AGE_CHOICES = (
        (NOT_SET, 'Not Set'),
        (TEENS, 'Teens'),
        (TWENTIES, 'Twenties'),
        (THIRTIES, 'Thirties'),
    )
    age = models.CharField(max_length=3,
                           choices=AGE_CHOICES,
                           default=NOT_SET)

    IN_REST = 'INR'
    STUDENT = 'STD'
    OFFICER = 'OFC'
    OCCUPATION_CHOICES = (
        (NOT_SET, 'Not Set'),
        (IN_REST, 'in Rest'),
        (STUDENT, 'Student'),
        (OFFICER, 'Office Worker'),
    )
    occupation = models.CharField(max_length=3,
                                  choices=OCCUPATION_CHOICES,
                                  default=NOT_SET,)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id

    def have_set(self, var):
        return eval('self.'+var) != self.NOT_SET

    def have_name_set(self):
        return len(self.name) != 0

    def have_gender_set(self):
        return self.gender != self.NOT_SET

    def have_age_set(self):
        return self.age != self.NOT_SET

    def increase_age(self):
        ages = self.AGE_CHOICES
        self.age = ages[ages.index(self.age)+1]

    def have_occupation_set(self):
        return self.occupation != self.NOT_SET
