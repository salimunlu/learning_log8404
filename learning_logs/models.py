from django.db import models


# Create your models here.
# Herbir veritabanı modeli = veritabanı tablosu

class Topic(models.Model):
    """A topic represents a field the user learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Learning log entries for a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return f"{self.text[:50]}..."

