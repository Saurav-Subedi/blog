from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import uuid

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField(upload_to='category',blank=True)
    description = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    description = RichTextField(blank=True,null=True)
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name_plural = 'Post'

    def limit_description(self):
        return self.description[:200] + '...'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            unique_id = uuid.uuid4().hex[:6]  
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{unique_id}-{counter}"
                counter += 1

            self.slug = slug  

        super().save(*args, **kwargs)
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='welcome.gif',null=True,blank=True)

    def __str__(self):
        return self.user.username


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

