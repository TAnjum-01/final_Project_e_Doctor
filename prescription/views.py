from django.shortcuts import render, redirect

from doctor.forms import doctors_form


# Create your views here.

def prescription(request):
    if request.method == 'POST':
        form = prescription(request.POST)
        form.save()

        return redirect('homepage')

    form = doctors_form()
    context = {
        'prescription': form,
    }
    return render(request, 'prescription.html', context)