

from django.db import models

class UserProfile(models.Model):
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.phone


# ---------------- COURSE MODEL ----------------
class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses/')
    language = models.CharField(max_length=50)
    price = models.IntegerField()
    old_price = models.IntegerField()
    discount = models.CharField(max_length=50)
    offer_text = models.CharField(max_length=200)
    is_live = models.BooleanField(default=False)
    video_url = models.URLField()

    def __str__(self):
        return self.title


# ---------------- CART MODEL ----------------
class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.phone} - {self.course.title}"
