# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm, DatasetUploadForm, VisualizationForm, DataColumnForm, DataPointForm
from .models import Dataset, Visualization, DataColumn, DataPoint

def home(request):
    if request.user.is_authenticated:
        datasets = Dataset.objects.filter(user=request.user)
        visualizations = Visualization.objects.filter(user=request.user)
        return render(request, 'dashboard.html', {'datasets': datasets, 'visualizations': visualizations})
    else:
        return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def upload_dataset(request):
    if request.method == 'POST':
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.user = request.user
            dataset.save()
            # Add data processing logic here if needed
            return redirect('home')
    else:
        form = DatasetUploadForm()
    return render(request, 'upload_dataset.html', {'form': form})

def create_visualization(request):
    if request.method == 'POST':
        form = VisualizationForm(request.POST)
        if form.is_valid():
            visualization = form.save(commit=False)
            visualization.user = request.user
            visualization.save()
            return redirect('home')
    else:
        form = VisualizationForm()
    return render(request, 'create_visualization.html', {'form': form})

def add_data_point(request, visualization_id):
    visualization = Visualization.objects.get(id=visualization_id)

    if request.method == 'POST':
        form = DataPointForm(request.POST)
        if form.is_valid():
            # Assuming data is a JSONField, update based on your actual data structure
            data = {
                'x_value': form.cleaned_data['x_value'],
                'y_value': form.cleaned_data['y_value'],
            }
            DataPoint.objects.create(visualization=visualization, data=data)
            return redirect('home')
    else:
        form = DataPointForm()
    return render(request, 'add_data_point.html', {'form': form, 'visualization': visualization})

def map_columns(request, visualization_id):
    visualization = Visualization.objects.get(id=visualization_id)

    if request.method == 'POST':
        form = DataColumnForm(request.POST)
        if form.is_valid():
            # Save the DataColumn based on the form data
            DataColumn.objects.create(
                visualization=visualization,
                column_name=form.cleaned_data['column_name'],
                data_type=form.cleaned_data['data_type'],
            )
            return redirect('home')
    else:
        form = DataColumnForm()
    return render(request, 'map_columns.html', {'form': form, 'visualization': visualization})
