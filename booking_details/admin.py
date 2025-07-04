from django.contrib import admin
from booking_details.models import bookings,view_review,upload_file
class bookings_admin(admin.ModelAdmin):
    list_dis=('name','guests','time','date','requests','code')
class review_admin(admin.ModelAdmin):
    list_rev=('reviewer','review')
class file_admin(admin.ModelAdmin):
    list_file=('file')
# Register your models here.
admin.site.register(bookings,bookings_admin)
admin.site.register(view_review,review_admin)
admin.site.register(upload_file,file_admin)