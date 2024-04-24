from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """docstring for User."""
    # Con esto hago que sobreescriba el modo de loguear. Ya no con username, si no que ahora con email
    # Esto se llama overwrite
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    

