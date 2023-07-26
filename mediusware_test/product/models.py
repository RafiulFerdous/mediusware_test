from django.db import models

# Create your models here.



class YourModelName(models.Model):
    id = models.BigAutoField(primary_key=True)  # bigint(20) unsigned
    title = models.CharField(max_length=225)    # varchar(225)
    sku = models.CharField(max_length=225)      # varchar(225)
    description = models.TextField()           # text
    created_at = models.DateTimeField(auto_now_add=True)   # timestamp (auto-filled on creation)
    updated_at = models.DateTimeField(auto_now=True)       # timestamp (auto-filled on update)

    def __str__(self):
        return self.title
