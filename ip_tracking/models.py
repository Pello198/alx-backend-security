from django.db import models
from django.utils import timezone
class SuspiciousIP(models.Model):
    ip_address = models.CharField(max_length=50)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address} - {self.reason}"
class RequestLog(models.Model):
    ip_address = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=timezone.now)
    path = models.CharField(max_length=255)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.ip_address} - {self.country} - {self.city} - {self.path}"
class RequestLog(models.Model):
    ip_address = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=timezone.now)
    path = models.CharField(max_length=255)

class BlockedIP(models.Model):
    ip_address = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.ip_address

class RequestLog(models.Model):
    ip_address = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=timezone.now)
    path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address} - {self.path} - {self.timestamp}"
