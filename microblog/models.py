from django.db import models


class Newblogposts(models.Model):
    title = models.TextField()
    body = models.TextField()
    day = models.TextField()
    time = models.TextField()
    
    def __unicode__(self):
        return self.name
        
class Comments(models.Model):
    name = models.TextField()
    comment = models.TextField()
    title = models.TextField()
    
    def __unicode__(self):
        return self.name
