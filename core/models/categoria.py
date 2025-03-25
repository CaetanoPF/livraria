from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

from .user import User
from .categoria import Categoria