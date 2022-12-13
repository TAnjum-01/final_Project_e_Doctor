from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from patient.forms import patients_form


# Create your views here.
def patient(request):
    if request.method == 'POST':
        form = patients_form(request.POST)
        form.save()

        return redirect('homepage')

    form = patients_form()
    context = {
        'patient_form': form,
    }
    return render(request, 'patients_info.html', context)

'''
def testing(request):
    mydata = patient.objects.values_list('p_id')
    template = loader.get_template('template.html')
    context = {
        'patient': mydata,
    }
    return HttpResponse(template.render(context, request))
'''