from django.db import models

class HomeCarusel(models.Model):
    name = models.CharField('HomeCarusel name', max_length=40)
    img = models.ImageField('HomeCarusel image', upload_to='media')
    info1 = models.CharField('HomeCarusel info_1', max_length=15)
    info2 = models.CharField('HomeCarusel info_2', max_length=15, blank = True)
    verified = models.ImageField('HomeCarusel verified image', upload_to='media', blank=True)
    
    def __str__(self):
        return self.name

class HomeTopic(models.Model):
    topic = models.CharField('HomeTopic topic', max_length=20)
    img = models.ImageField('HomeTopic image', upload_to='media')
    i_count = models.CharField('HomeTopic i_count', max_length=25)

    def __str__(self):
        return self.name
