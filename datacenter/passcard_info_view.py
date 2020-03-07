from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        visit_info = {
            'entered_at' : visit.entered_at,
            'duration' : visit.format_duration(),
            'is_strange' : visit.is_long(),
        }
        this_passcard_visits.append(visit_info)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
