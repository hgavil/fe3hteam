from django.contrib import admin
from .models import Feteamapp, Unit, UnitClass, Ability, Proficiency

# Register your models here.
admin.site.register(Feteamapp)
admin.site.register(Unit)
admin.site.register(UnitClass)
admin.site.register(Ability)
admin.site.register(Proficiency)
