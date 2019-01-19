from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
from django.views.generic import TemplateView
from .models import AddRover,SubTeam, TeamAdvisor, Member, TeamLeader, MembersPage as MP
# Create your views here.
class OldRoverPage(TemplateView):
    template_name = 'old_rover.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            leader = TeamLeader.objects.get().member
        except ObjectDoesNotExist:
            leader = None
        extra_context = {
            'roveryear': AddRover.objects.prefetch_related('member_of').all(),
            'subteams': SubTeam.objects.prefetch_related('members').all(),
            'advisors': TeamAdvisor.objects.all(),
            'leader': leader,
            'subteamless': Member.objects.filter(subteam=None),
            'page': MP.objects.get(),
        }
        context.update(extra_context)
        return context
