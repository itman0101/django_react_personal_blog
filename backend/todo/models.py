from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    completed = models.BooleanField(default = False)

    def _str_ (self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length = 200)
    story= models.TextField()


    def _str_ (self):
        return self.name


class Project(models.Model):
    project_title = models.CharField(max_length = 200)
    project_description = models.TextField()
    project_start = models.DateField()
    project_end = models.DateField()
    project_author = models.CharField(max_length = 50)

    def _str_(self):
        return self.project_title

class Post(models.Model):
    post_title = models.CharField(max_length = 200)
    post_image = models.ImageField()
    post_brief = models.TextField()
    post_content = models.TextField()
    post_publish_date = models.DateField()
    post_author = models.CharField(max_length = 20)
    post_category=models.CharField(max_length = 10)

    def _str_(self):
        return self.post_title



class Comment(models.Model):
    comment_id = models.CharField(max_length=100)
    comment_content = models.TextField()
    comment_author_id = models.CharField(max_length=100)
    comment_email = models.EmailField()

    def _str_(self):
        return self.comment_id
