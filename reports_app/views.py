from django.shortcuts import render, redirect
from .forms import reportsForm
from .forms import SearchDiseaseForm
from .forms import SearchPestForm
from .forms import CountyStatusForm
from .models import reports
from counties_app.models import counties
from diseases_app.models import diseases
from pests_app.models import pests
from django.db.models import Sum
from django.utils.dateparse import parse_date
from django.db.models import Count
from django.http import JsonResponse
from django.http import JsonResponse
import json
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

#check county status
@never_cache
@login_required
def countyStatus(request):
    if request.method == 'POST':
        form = CountyStatusForm(request.POST)
        if form.is_valid():
            countyName = form.cleaned_data['countyName']
            created_at = form.cleaned_data['created_at']
            updated_at = form.cleaned_data['updated_at']

            reports_data = reports.objects.filter(countyName=countyName)
            
            # Apply date filtering if start_date and end_date are provided
            if created_at:
                reports_data = reports_data.filter(created_at__gte=created_at)
            if updated_at:
                reports_data = reports_data.filter(updated_at__lte=updated_at)

            reports_data = reports_data.values('diseaseName', 'recorded_by').annotate(num_cases=Count('diseaseName'))

            total_cases = sum(entry['num_cases'] for entry in reports_data)
            data_list = [{'disease': entry['diseaseName'], 'num_cases': entry['num_cases'], 'recorded_by': entry['recorded_by']} for entry in reports_data]

            diseases = [entry['diseaseName'] for entry in reports_data]
            num_cases = [entry['num_cases'] for entry in reports_data]

            # Sort data_list based on num_cases in descending order
            data_list.sort(key=lambda x: x['num_cases'], reverse=True)

            return render(request, 'status_results.html', {'countyName': countyName, 'total_cases': total_cases, 'data_list': data_list, 'diseases': json.dumps(diseases), 'num_cases': json.dumps(num_cases)})
    else:
        form = CountyStatusForm()

    return render(request, 'search_status.html', {'form': form})


@never_cache
@login_required
def findDisease(request):
    if request.method == 'POST':
        form = SearchDiseaseForm(request.POST)
        if form.is_valid():
            diseaseName = form.cleaned_data['diseaseName']
            created_at = form.cleaned_data['created_at']
            updated_at = form.cleaned_data['updated_at']

            reports_data = reports.objects.filter(diseaseName=diseaseName)
            
            # Apply date filtering if start_date and end_date are provided
            if created_at:
                reports_data = reports_data.filter(created_at__gte=created_at)
            if updated_at:
                reports_data = reports_data.filter(updated_at__lte=updated_at)

            reports_data = reports_data.values('countyName', 'recorded_by').annotate(num_cases=Count('countyName'))

            total_cases = sum(entry['num_cases'] for entry in reports_data)
            data_list = [{'county': entry['countyName'], 'num_cases': entry['num_cases'], 'recorded_by': entry['recorded_by']} for entry in reports_data]

            counties = [entry['countyName'] for entry in reports_data]
            num_cases = [entry['num_cases'] for entry in reports_data]

            # Sort data_list based on num_cases in descending order
            data_list.sort(key=lambda x: x['num_cases'], reverse=True)

            return render(request, 'disease_results.html', {'diseaseName': diseaseName, 'total_cases': total_cases, 'data_list': data_list, 'counties': json.dumps(counties), 'num_cases': json.dumps(num_cases)})
    else:
        form = SearchDiseaseForm()

    return render(request, 'search_disease.html', {'form': form})

@never_cache
@login_required
def findPest(request):
    if request.method == 'POST':
        form = SearchPestForm(request.POST)
        if form.is_valid():
            pestName = form.cleaned_data.get('pestName')
            created_at = form.cleaned_data['created_at']
            updated_at = form.cleaned_data['updated_at']

            reports_data = reports.objects.filter(pestName=pestName)
            
            # Apply date filtering if start_date and end_date are provided
            if created_at:
                reports_data = reports_data.filter(created_at__gte=created_at)
            if updated_at:
                reports_data = reports_data.filter(updated_at__lte=updated_at)

            reports_data = reports_data.values('countyName', 'recorded_by').annotate(num_cases=Count('countyName'))

            total_cases = sum(entry['num_cases'] for entry in reports_data)
            data_list = [{'county': entry['countyName'], 'num_cases': entry['num_cases'], 'recorded_by': entry['recorded_by']} for entry in reports_data]

            counties = [entry['countyName'] for entry in reports_data]
            num_cases = [entry['num_cases'] for entry in reports_data]

            # Sort data_list based on num_cases in descending order
            data_list.sort(key=lambda x: x['num_cases'], reverse=True)

            return render(request, 'pest_results.html', {'pestName': pestName, 'total_cases': total_cases, 'data_list': data_list, 'counties': json.dumps(counties), 'num_cases': json.dumps(num_cases)})
    else:
        form = SearchPestForm()
    
    return render(request, 'search_pest.html', {'form': form})


#create reports
@never_cache
@login_required
def create_report(request):
    if request.method == "POST":
        form = reportsForm(request.POST, user=request.user)
        if form.is_valid():
            try:
                # Capture latitude and longitude from POST data
                latitude = request.POST.get('latitude')
                longitude = request.POST.get('longitude')
                
                # Save the form data, including the location
                report = form.save(commit=False)
                report.latitude = latitude
                report.longitude = longitude
                report.save()
                
                return redirect('searchReport/')
            except Exception as e:
                print(f"Error: {e}")
    else:
        form = reportsForm(user=request.user)
    
    return render(request, 'createReport.html', {'form': form})



#search reports
@never_cache
@login_required
def retrieve_report(request):
    rpt = reports.objects.filter(recorded_by=request.user.username)
    return render(request, 'searchReport.html', {'reports': rpt})

#update reports
@never_cache
@login_required
def update_report(request, pk):
    rpt = reports.objects.get(id=pk)
    form = reportsForm(instance=rpt)

    if request.method == 'POST':
        form = reportsForm(request.POST, instance=rpt)
        if form.is_valid():
            form.save()
            return redirect('/searchReport')

    context = {
        'rpt': rpt,
        'form': form,
    }
    return render(request, 'updateReport.html', context)


#delete reports
@never_cache
@login_required
def delete_report(request, pk):
    rpt = reports.objects.get(id=pk)

    if request.method == 'POST':
        rpt.delete()
        return redirect('/searchReport')

    context = {
        'rpt': rpt,
    }
    return render(request, 'removeReport.html', context)

def test(request):
    return render(request, 'test.html')