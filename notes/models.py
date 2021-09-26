from django.db import models


class Tag(models.Model):
    tag_str = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.tag_str

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    id= models.AutoField(primary_key=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)  # https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey.on_delete

    def __str__(self):
        id_title = '{}.{}'.format(self.id,self.title)
        return id_title

