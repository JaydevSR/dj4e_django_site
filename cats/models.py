from django.db import models
from django.core.validators import MinLengthValidator

class Breed(models.Model):
    name = models.CharField(
                max_length=200,
                validators=[MinLengthValidator(2, "Breed must atleast be 2 characteers")]
            )

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(
                max_length=200,
                validators=[MinLengthValidator(2, "Nickname must atleast be 2 characters")]
            )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname

