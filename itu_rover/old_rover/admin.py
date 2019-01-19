from django.contrib import admin

from .models import Member, SubTeam, TeamLeader, TeamAdvisor, MembersPage, AddRover

models = [Member, SubTeam, TeamLeader, TeamAdvisor, MembersPage, AddRover]
admin.site.register(models)

