from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password):
        """Creates a new `UserProfile` object."""

        if not email:
            raise ValueError('Users must have an email address.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new super user."""

        user = self.create_user(email, name, password)
        user.is_superuser, user.is_staff = True, True
        user.save(using=self._db)        

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a user's full name."""

        return self.name
        
    def get_short_name(self):
        """Used to get a user's short name."""

        return self.name

    def __str__(self):
        """Used to convert object to string."""
        
        return self.email

