from django.shortcuts import render, redirect

from doctor.forms import doctors_form


# Create your views here.

def doctor(request):
    if request.method == 'POST':
        form = doctors_form(request.POST)
        form.save()

        return redirect('homepage')

    form = doctors_form()
    context = {
        'doctor_form': form,
    }
    return render(request, 'doctors_info.html', context)