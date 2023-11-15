from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.



class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default="")
    #status= models.CharField(choices=CATEGORY, max_length=10, default= DEFAULT)

    def __str__(self):
        return self.title

class Post(models.Model):
    user = models.ForeignKey('auth.User',null=True, default=None, related_name = 'post', on_delete= models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    publish_date = models.DateTimeField(verbose_name= 'Publish Date', auto_now_add = True) 
    image = models.ImageField(null=True, blank=True, upload_to='post')
    slug= models.SlugField(unique= True, editable= False, max_length=130)
    #category = models.CharField(choices=CATEGORY, max_length=30, default='software')
    category= models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug= slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1 
        while Post.objects.filter(slug= unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter+= 1
        return unique_slug
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)
    
    def yearpublished(self):
        return self.publish_date.strftime('%d %b %Y')
    
    class Meta:
        ordering = ['-publish_date', 'id']

#sql injection engelleyici method var djangonun