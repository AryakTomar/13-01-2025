# from django.db import models

# # Create your models here.
# class Customer(models.Model):
#     name = models.CharField(max_length = 100)
#     email = models.EmailField(unique = True)
#     phone = models.CharField(max_length=10)
#     address = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
# #Above code is working fine
# -----------------------------------------------------------


from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20, default="")

    telegram_chat_id = models.CharField(max_length=50, null=True, blank=True)

    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    


    
