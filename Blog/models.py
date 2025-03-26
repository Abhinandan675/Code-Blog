from django.db import models

# Create your models here.
class Blogpost(models.Model):
    sno=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=20)
    Author=models.CharField(max_length=12)
    Slug=models.CharField(max_length=50)
    content=models.TextField()
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return  self.Title + ' - ' + self.Author #to dispaly name and email of the user in database
