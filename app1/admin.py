from django.contrib import admin

from app1.models import mr_user,dr_user,visit,testing,slide

# Register your models here.

admin.site.register(mr_user)

admin.site.register(dr_user)

admin.site.register(visit)
admin.site.register(testing)
admin.site.register(slide)


