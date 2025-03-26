from django.db import models

# Create your models here.
# table for storing the data from contact us page

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=20)
    Phone=models.CharField(max_length=12)
    Emails=models.CharField(max_length=50)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from ' +  self.Name + ' - ' + self.Emails #to dispaly name and email of the user in database
