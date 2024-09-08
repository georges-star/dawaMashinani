from django.shortcuts import render, redirect
from .forms import pestsForm
from .models import pests
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

#create pests
@never_cache
@login_required
def create_pest(request):
    if request.method == "POST":
        form = pestsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('searchPest/')
            except:
                pass
    else:
        form = pestsForm()
    return render(request, 'createPest.html', {'form':form})

#search pests
@never_cache
@login_required
def retrieve_pest(request):
    pest=pests.objects.all()
    return render(request, 'searchPest.html', {'pests': pest})

#update pests
@never_cache
@login_required
def update_pest(request,pk):
    pest = pests.objects.get(id=pk)
    form = pestsForm(instance=pest)

    if request.method == 'POST':
        form = pestsForm(request.POST, instance=pest)
        if form.is_valid():
            form.save()
            return redirect('/searchPest')

    context = {
        'pest': pest,
        'form': form,
    }
    return render(request,'updatePest.html',context)

#delete pests
@never_cache
@login_required
def delete_pest(request, pk):
    pest = pests.objects.get(id=pk)

    if request.method == 'POST':
        pest.delete()
        return redirect('/searchPest')

    context = {
        'pest': pest,
    }
    return render(request, 'removePest.html', context)

