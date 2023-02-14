from django.db import models

''' люди - общая информация '''
class HomeCarusel(models.Model):
    name = models.CharField('HomeCarusel name', max_length=40)
    img = models.ImageField('HomeCarusel image', upload_to='media')
    info1 = models.CharField('HomeCarusel info_1', max_length=15)
    info2 = models.CharField('HomeCarusel info_2', max_length=15, blank = True)
    boolean = models.BooleanField('Nout bool')
    ''' verified = models.ImageField('HomeCarusel verified image', upload_to='media', blank=True) '''
    
    def __str__(self):
        return self.name

''' Жанр - группа '''
class HomeGenre(models.Model):
    topic = models.CharField('HomeGenre topic', max_length=20)
    img = models.ImageField('HomeGenre image', upload_to='media')
    i_count = models.CharField('HomeGenre i_count', max_length=25)    
    ''' Надпись сверху листинг страницы '''
    story = models.TextField('HomeGenre story') 
    slug = models.SlugField('HomeGenre link', unique=True, blank=True)

    def __str__(self):
        return self.topic


''' Объект - отдельный подкаст '''
class HomeEpisode(models.Model):
    homegenre = models.ForeignKey(HomeGenre, on_delete=models.CASCADE, related_name='Full_list')
    name = models.CharField('HomeEpisode name', max_length=40)
    img = models.ImageField('HomeEpisode image', upload_to='media/podcast_poster')
    info = models.CharField('HomeEpisode info', max_length=115)
    duration = models.PositiveIntegerField('HomeEpisode duration (min)')
    episode_count = models.PositiveIntegerField('HomeEpisode episode_count')
    author = models.CharField('HomeEpisode author', max_length=40, blank=False)
    author_info = models.CharField('HomeEpisode author_info', max_length=20)
    author_img = models.ImageField('HomeEpisode author_img', upload_to='media/home__auther')
    story = models.TextField('HomeGenre story')
    
    def __str__(self):
        return self.name


