from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Team)
admin.site.register(Stadium)
admin.site.register(Player)
admin.site.register(Matchup)
admin.site.register(Stat)
admin.site.register(Roster)
admin.site.register(Score)