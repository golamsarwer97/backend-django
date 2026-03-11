import datetime

from django.db import models
from django.utils import timezone

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text   
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.

# PRIORITY = [
#     ("L","Low"),
#     ("M","Medium"),
#     ("H","High"),
# ]

# class Question(models.Model):
#     title       = models.CharField(max_length=200)
#     question    = models.TextField()
#     priority    = models.CharField(max_length=1,choices = PRIORITY)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "The Question"
#         verbose_name_plural = "People Questions"
#         # ordering = ['-id']  
    
