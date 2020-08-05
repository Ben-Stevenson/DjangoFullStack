from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
#used to limit rating so we only have 1 to 5.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class Genre(models.Model):
	genreName = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	slug = models.SlugField()
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.genreName)
		super(Genre, self).save(*args, **kwargs)
		
	class Meta:
		verbose_name_plural = 'genres'
	def __unicode__(self):
		return self.genreName
	def __str__(self):
		return self.genreName
		
class addAlbum(models.Model):
	genre = models.ForeignKey(Genre)
	title = models.CharField(max_length=128)
	artist = models.CharField(max_length=128)
	image = models.ImageField(upload_to='album_images', default='profile_images/blank.png')
	slug = models.SlugField(unique=True)
	
	def get_rating(self):
		try:
			r = addReview.objects.filter(album=self)
			value = r.aggregate(Avg('rating')).values()[0]
			return value
		except addReview.DoesNotExist:
			return 1
			
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(addAlbum, self).save(*args, **kwargs)
		
	class Meta:
		verbose_name_plural = 'Albums'
		
	
	def __str__(self): 
		return self.title
	

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class addReview(models.Model):
	album = models.ForeignKey(addAlbum)
	username = models.ForeignKey(User)
	review = models.CharField(max_length=128, unique=True)
	rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
	slug = models.SlugField(unique=True)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.review)
		super(addReview, self).save(*args, **kwargs)
		
	class Meta:
		verbose_name_plural = 'Reviews'
		unique_together = ('album','username',)
		
	def __str__(self):
		return self.review