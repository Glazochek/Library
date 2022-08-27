from datetime import timedelta
from django.db import models
from django.utils.timezone import now


class Project(models.Model):
    users_id = models.CharField(max_length=64, default='-')
    name = models.CharField(verbose_name='имя', max_length=64, unique=True, default='-')
    link = models.CharField(max_length=64, default='-')

    def __str__(self):
        return self.name


class TODO(models.Model):
    text = models.CharField(max_length=256, default='-')
    data_create = models.DateTimeField(default=now())
    data_update = models.DateTimeField(default=(now() + timedelta(hours=48)))
    user = models.ForeignKey(Project, unique=True, null=False, db_index=True, on_delete=models.CASCADE, default='-')
    status = models.BooleanField(db_index=True, verbose_name='активна', default=True)

    def __str__(self):
        return self.text

