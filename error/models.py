from django.db import models


# Create your models here.
class ModelParent(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Alphabet(models.Model):
    name = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class ModelInline(models.Model):
    parent = models.ForeignKey(ModelParent, on_delete=models.CASCADE, related_name="inline_parent")
    text = models.ManyToManyField(Alphabet)

    def __str__(self):
        return self.text
