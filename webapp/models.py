from django.db import models



#Category Model
class Category(models.Model):
    name = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

#Record Model
class Record(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    phone = models.IntegerField()
    tall = models.IntegerField()
    weight = models.IntegerField()
    address = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name +' '+ self.last_name 
   
    


