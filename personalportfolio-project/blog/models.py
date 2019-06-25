from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

# Create a blog model (title; pub_date; body; image)
# Add blog app to settings
# Create a migration
# Migrate
# Add to the admin
