from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class  Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    title =models.CharField(max_length=200)
    description = models.TextField()
    complete =models.BooleanField(default=False)
    created =models.DateTimeField(auto_now_add=True)

    #Gives string representation of the object
    def __str__(self) -> str:
        return  self.title
    
    # Any complete items will go down the bottom of the table
    class Meta:
        ordering =['complete']