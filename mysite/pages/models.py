from django.db import models

class HomeCarusel(models.Model):
    name = models.CharField('HomeCarusel name', max_length=40)
    img = models.ImageField('HomeCarusel image', upload_to='media')
    info1 = models.CharField('HomeCarusel info_1', max_length=15)
    info2 = models.CharField('HomeCarusel info_2', max_length=15, blank = True)
    # verified = models.ImageField('HomeCarusel verified image', upload_to='media', blank=True)
    
    def __str__(self):
        return self.name

class HomeTopic(models.Model):
    topic = models.CharField('HomeTopic topic', max_length=20)
    img = models.ImageField('HomeTopic image', upload_to='media')
    i_count = models.CharField('HomeTopic i_count', max_length=25)
    story = models.TextField('HomeTopic story')

    def __str__(self):
        return self.topic

class HomeLatestEpisode(models.Model):
    name = models.CharField('HomeLatestEpisode name', max_length=40)
    img = models.ImageField('HomeLatestEpisode image', upload_to='media/podcast_poster')
    info = models.CharField('HomeLatestEpisode info', max_length=115)
    duration = models.PositiveIntegerField('HomeLatestEpisode duration (min)')
    episode_count = models.PositiveIntegerField('HomeLatestEpisode episode_count')
    author = models.CharField('HomeLatestEpisode author', max_length=40, blank=False)
    author_info = models.CharField('HomeLatestEpisode author_info', max_length=20)
    author_img = models.ImageField('HomeLatestEpisode author_img', upload_to='media/home_latest_auther')


    def __str__(self):
        return self.name

class HomeTrendingEpisode(models.Model):
    name = models.CharField('HomeTrendingEpisode name', max_length=40)
    img = models.ImageField('HomeTrendingEpisode image', upload_to='media/podcast_poster')
    info = models.CharField('HomeTrendingEpisode info', max_length=115)
    author = models.CharField('HomeTrendingEpisode author', max_length=40)
    author_info = models.CharField('HomeLatestEpisode author_info', max_length=20)
    author_img = models.ImageField('HomeTrendingEpisode author_img', upload_to='media/home_latest_auther')


    def __str__(self):
        return self.name

class AboutPodcaster(models.Model):
    name = models.CharField('HomeCarusel name', max_length=40)
    img = models.ImageField('HomeCarusel image', upload_to='media')
    info1 = models.CharField('HomeCarusel info_1', max_length=15)
    info2 = models.CharField('HomeCarusel info_2', max_length=15, blank = True)