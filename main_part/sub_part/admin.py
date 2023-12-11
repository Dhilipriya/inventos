from django.contrib import admin

# Register your models here.
from . models import contact_table,reg_table,add_user
admin.site.register(contact_table)
admin.site.register(reg_table)
admin.site.register(add_user)
