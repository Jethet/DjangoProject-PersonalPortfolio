from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

# Create a blog model (title; pub_date; body; image)
# Add blog app to settings
# Create a migration
# Migrate
# Add to the admin

"""
TO GET THE BLOGS ONLINE:
* create a for loop in the /allblogs.html file
* in blog/views, import the Blog class:
     from .models import Blog
  in blog/views make a variable for objects created with this class:
     blogs = Blog.objects
  add this variable to the return code line:
     return render(request, 'blog/allblogs.html', {'blogs':blogs})

This is similar to what is done to upload the jobs cards.
"""
