from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()
    isbn = models.CharField(max_length=100)
    copies = models.IntegerField()

    def __str__(self):
        return self.title


class LibUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(LibUser, on_delete=models.CASCADE)
    date_rented = models.DateTimeField()
    date_due = models.DateTimeField()
    date_returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.date_rented
