from django.db import models


class Author(models.Model):

    username = models.CharField(unique=True, null=False, db_index=True, max_length=100)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    birthday_year = models.PositiveIntegerField()
    email = models.TextField(unique=True, verbose_name='email', max_length=100, blank=True)

    def __str__(self):
        return self.username
