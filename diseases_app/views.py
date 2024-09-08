from django.shortcuts import render, redirect
from .forms import diseasesForm
from .models import diseases
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

#create diseases
@never_cache
@login_required
def create_disease(request):
    if request.method == "POST":
        form = diseasesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/searchDisease')
            except:
                pass
    else:
        form = diseasesForm()
    return render(request, 'createDisease.html', {'form':form})

#search disease
@never_cache
@login_required
def retrieve_disease(request):
    disease=diseases.objects.all()
    return render(request, 'searchDisease.html', {'diseases': disease})

#update disease
@never_cache
@login_required
def update_disease(request,pk):
    disease = diseases.objects.get(id=pk)
    form = diseasesForm(instance=disease)

    if request.method == 'POST':
        form = diseasesForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('/searchDisease')

    context = {
        'disease': disease,
        'form': form,
    }
    return render(request,'updateDisease.html',context)

#delete disease
@never_cache
@login_required
def delete_disease(request, pk):
    disease = diseases.objects.get(id=pk)

    if request.method == 'POST':
        disease.delete()
        return redirect('/searchDisease')

    context = {
        'disease': disease,
    }
    return render(request, 'removeDisease.html', context)