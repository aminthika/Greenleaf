from django.contrib import admin
from greenleaf.models import Rewild, RewildPhoto

class RewildAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['name', 'trees', 'location', 'email']
=======
    list_display = ['trees', 'location', 'email']
>>>>>>> 75b29a0e14cae0007467984f1c224b215ff368a8

class RewildPhotoAdmin(admin.ModelAdmin):
    list_display = ['rewild', 'image']


admin.site.register(Rewild, RewildAdmin)
admin.site.register(RewildPhoto, RewildPhotoAdmin)
