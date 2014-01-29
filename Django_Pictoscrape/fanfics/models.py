from django.db import models
from django.utils import timezone

class FanFic(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	pub_date = models.DateTimeField('date published', default=timezone.now())
	def __unicode__(self):
		return self.title
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Keyword(models.Model):
	story = models.ForeignKey(FanFic)
	key_word = models.CharField(max_length=200)
	def __unicode__(self):
		return self.key_word