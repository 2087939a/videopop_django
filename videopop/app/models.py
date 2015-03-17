from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import ast

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    score = models.IntegerField(max_length = 128)
    def __unicode__(self):
           return self.user.name
        
class Video(models.Model):
	url = models.URLField()
	correctAnswer = models.CharField(max_length = 128)
		
class Game(models.Model):
	game_mode = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True)
	url = models.ForeignKey(Video)
	
	def __unicode__(self):
		return self.game_mode
	
class Score(models.Model):
	user = models.ForeignKey(User)
	game = models.ForeignKey(Game)
	score = models.IntegerField(default=0)
	
	
	def __unicode__(self):
		return str(self.score)
			
class ListField(models.TextField):                 #stolen from 												
    __metaclass__ = models.SubfieldBase		   #http://stackoverflow.com/questions/22340258/django-list-field-in-model
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

	
class RankingTable(models.Model):
	best_scores = ListField()
	
	
