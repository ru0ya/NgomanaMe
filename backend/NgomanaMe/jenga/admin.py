from django.contrib import admin

from jenga.models import Category, Tutorial, Step, Material, Comment


admin.site.register(Category)
admin.site.register(Tutorial)
admin.site.register(Step)
admin.site.register(Material)
admin.site.register(Comment)
