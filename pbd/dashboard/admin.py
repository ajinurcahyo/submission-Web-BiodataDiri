from django.contrib import admin

from . models import Rth
from . models import Penghijauan
from . models import Taman

admin.site.register(Rth)
admin.site.register(Penghijauan)
admin.site.register(Taman)