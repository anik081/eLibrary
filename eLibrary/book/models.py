from django.db import models


# Create your models here.
class Book(models.Model):
	book_title = models.CharField(max_length =250)
	book_author = models.CharField(max_length=250)
	book_publisher = models.CharField(max_length =300)
	book_image = models.FileField()



	def __str__(self):
		return self.book_name+'-'+self.book_author