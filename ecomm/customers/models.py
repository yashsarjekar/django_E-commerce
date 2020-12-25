from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.email

    @staticmethod
    def check_user_exist(email_id):
        try:
            em = Customer.objects.filter(email=email_id)
            #print(len(em))
            if len(em) == 0:
                return True
            else:
                return "User already Exist"
        except Customer.DoesNotExist:
            return "User already Exist"
