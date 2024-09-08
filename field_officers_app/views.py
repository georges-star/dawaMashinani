from django.shortcuts import render, redirect
from .forms import field_officersForm
from .models import field_officers
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache



#create field officer
@never_cache
@login_required
def create_field_officer(request):
    if request.method == "POST":
        form = field_officersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('searchOfficer/')
            except:
                pass
    else:
        form = field_officersForm()
    return render(request, 'createOfficer.html', {'form':form})

#search field officers
@never_cache
@login_required
def retrieve_field_officer(request):
    field_officer=field_officers.objects.all()
    return render(request, 'searchOfficer.html', {'field_officers': field_officer})

#update field officer
@never_cache
@login_required
def update_field_officer(request,pk):
    officer = field_officers.objects.get(id=pk)
    form = field_officersForm(instance=officer)

    if request.method == 'POST':
        form = field_officersForm(request.POST, instance=officer)
        if form.is_valid():
            form.save()
            return redirect('/searchOfficer')

    context = {
        'officer': officer,
        'form': form,
    }
    return render(request,'updateOfficer.html',context)

#delete field officer
@never_cache
@login_required
def delete_field_officer(request, pk):
    officer = field_officers.objects.get(id=pk)

    if request.method == 'POST':
        officer.delete()
        return redirect('/searchOfficer')

    context = {
        'officer': officer,
    }
    return render(request, 'removeOfficer.html', context)