from django.db import models
from django.utils import timezone
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Film(models.Model):
    # Fields
    title = models.CharField(max_length=200, verbose_name="Title")
    plot = models.TextField(blank=True, null=True, verbose_name="Plot")
    release_date = models.DateField(default=timezone.now, help_text="Please use the following format: <em>YYYY-MM-DD</em>.", verbose_name="Release date")
    runtime = models.IntegerField(blank=True, verbose_name="Runtime")
    rate = models.FloatField(default=5.0, verbose_name="Rate")
    poster = models.ImageField(blank=True, null=True, verbose_name="Poster")

    # Metadata
    class Meta:
        ordering = ["-release_date", "title"]

    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular instance of Film."""
        return reverse('film-detail', args=[str(self.id)])