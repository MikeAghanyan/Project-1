from django.db import models

class ContactUs(models.Model):
    full_name = models.CharField('ContactUs full_name', max_length=70)
    email = models.EmailField('ContactUs email')
    company = models.CharField('ContactUs company', max_length=70)
    text = models.TextField('ContactUs text')

    def __str__(self):
        return self.email