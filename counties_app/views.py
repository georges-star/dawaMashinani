from django.shortcuts import render, redirect
from .forms import countiesForm
from .models import counties
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

#create counties
@never_cache
@login_required
def create_county(request):
    if request.method == "POST":
        form = countiesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('retrieve_county')
            except:
                pass
    else:
        form = countiesForm()
    return render(request, 'createCounty.html', {'form':form})

#search counties
@never_cache
@login_required
def retrieve_county(request):
    cty=counties.objects.all().order_by('county_name').values()
    return render(request, 'searchCounty.html', {'counties': cty})

#update counties
@never_cache
@login_required
def update_county(request,pk):
    cty = counties.objects.get(id=pk)
    form = countiesForm(instance=cty)

    if request.method == 'POST':
        form = countiesForm(request.POST, instance=cty)
        if form.is_valid():
            form.save()
            return redirect('retrieve_county')

    context = {
        'cty': cty,
        'form': form,
    }
    return render(request,'updateCounty.html',context)

#delete county
@never_cache
@login_required
def delete_county(request, pk):
    cty = counties.objects.get(id=pk)

    if request.method == 'POST':
        cty.delete()
        return redirect('retrieve_county')

    context = {
        'cty': cty,
    }
    return render(request, 'removeCounty.html', context)

