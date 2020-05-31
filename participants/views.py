from django.shortcuts import get_object_or_404, redirect, render
from .models import EnvironmentExposures, GeneticMutations, Participants


def index(request):
    return render(request, 'form.html')


def participants(request):
    participants = Participants.objects.all()

    return render(request, 'participants.html', {'participants': participants})


def new_participant(request):
    if request.method == 'POST':
        participant = Participants.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            siblings=request.POST['siblings']
        )

        exposures = request.POST['exposures'].split()
        for exposure in exposures:
            e, created = EnvironmentExposures.objects.get_or_create(
                name=exposure)
            participant.exposures.add(e)

        mutations = request.POST['mutations'].split()
        for mutation in mutations:
            m, created = GeneticMutations.objects.get_or_create(name=mutation)
            participant.mutations.add(m)

        return redirect('/participants')
    else:
        return redirect('/')


def update_participant(request):
    if request.method == 'POST':
        Participants.objects.filter(pk=request.POST['id']).update(
            status=request.POST['status'])

    return redirect('/participants')
