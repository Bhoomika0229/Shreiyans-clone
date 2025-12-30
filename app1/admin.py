from django.contrib import admin
from .models import UserProfile, Course, Cart


# -------- USER PROFILE --------
admin.site.register(UserProfile)


# -------- COURSE ADMIN --------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'language', 'is_live')
    search_fields = ('title',)
    list_filter = ('language', 'is_live')


# -------- CART ADMIN --------
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    search_fields = ('user__phone', 'course__title')
