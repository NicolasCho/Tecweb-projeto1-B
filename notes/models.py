from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    id= models.AutoField(primary_key=True)

    def __str__(self):
        id_title = '{}.{}'.format(self.id,self.title)
        return id_title

