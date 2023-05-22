from django.db import models
from django.contrib.auth.models import User
from project_pack.proyecto import Proyecto

# Create your models here.
class LDCxPF(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    C = models.SmallIntegerField()
    CPP = models.SmallIntegerField()
    JAVA = models.SmallIntegerField()
    JAVASCRIPT = models.SmallIntegerField()
    JSP = models.SmallIntegerField()
    SQL = models.SmallIntegerField()
    PYTHON = models.SmallIntegerField()
    CSHARP = models.SmallIntegerField()
    NET = models.SmallIntegerField()
    GO = models.SmallIntegerField()
    PHP = models.SmallIntegerField()

    def __str__(self):
        return str(self.user) + str(self.C) + str(self.CPP) + str(self.JAVA)