from django.db import models

# Create your models here.

#Category model
class Catagory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    urls = models.CharField(max_length=100)
    image = models.ImageField(upload_to='catagory/')
    add_date= models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

#Post Model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    urls = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')
    add_date= models.DateTimeField(auto_now_add=True,null=True)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

