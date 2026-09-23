from django.db import models

class Movie(models.Model):
    CONTENT_TYPES = [('movie', 'Movie'), ('series', 'Series')]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES, default='movie')
    genre = models.CharField(max_length=120, blank=True)
    release_year = models.PositiveIntegerField(default=2025)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=8.0)
    duration = models.CharField(max_length=30, blank=True)
    maturity = models.CharField(max_length=20, default='U/A 13+')
    poster_url = models.URLField(blank=True)
    backdrop_url = models.URLField(blank=True)
    trailer_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return self.title
