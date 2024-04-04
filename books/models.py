import uuid     # generates a long string of ID instead of just 1, 2, 3 and so on for the books
from django.contrib.auth import get_user_model      # reviews model
from django.db import models
from django.urls import reverse # new

class Book(models.Model):
    id = models.UUIDField (
        primary_key=True,
        default=uuid.uuid4,     # for creating a unique id in every book
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)  # users media
    # to upload all types of file, change to FileField

    class Meta:
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    def __str__(self):
            return self.title

    def get_absolute_url(self):
            return reverse('book_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': str(self.pk)})


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.review

    class Meta:     # for indexing, allows faster searches and only applied to primary key
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
        permissions = [
            ("special_status", "Can read all books"),
        ]



