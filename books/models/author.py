from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    telegram_account_id = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
