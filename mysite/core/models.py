from django.db import models
from django.utils.text import slugify


CATEGORY_CHOICES = (
    ('SD', '480p'),
    ('HD', '720p'),
    ('FHD', '1080')
)
# Create your models here.
class Vibg(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length = 100, null = True, blank = True)
	description = models.CharField(max_length=400)
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
	date_added = models.DateTimeField(auto_now_add=True)
	video = models.FileField(upload_to='video/')
	thumbnail = models.FileField(upload_to='images/', null=True, blank=True)

	def __str__(self):
		return self.title
		
	def delete(self, *args, **kwargs):
		self.video.delete()
		self.thumbnail.delete()
		super().delete(*args, **kwargs)

	def _get_unique_slug(self):
		slug = slugify(self.title)
		unique_slug = slug
		num = 1
		while Vibg.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug,num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)



		