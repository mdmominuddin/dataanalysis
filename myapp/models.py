# models.py

from django.db import models
from django.contrib.auth.models import User
import pandas as pd

class Dataset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='datasets/')

    def __str__(self):
        return self.name

    def full_data(self):
        # Load CSV data using pandas
        return pd.read_csv(self.file.path)

    def save_data(self, data):
        # Save the entire dataset to the database
        # This assumes the data parameter is a pandas DataFrame
        data.to_csv(self.file.path, index=False)

class Visualization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def full_data(self):
        # Combine all DataPoint instances associated with this Visualization
        data_points = self.datapoint_set.all()
        data = [data_point.data for data_point in data_points]
        return pd.DataFrame(data)

    def analyze_data(self):
        # Assuming some analysis logic here
        data_points = self.datapoint_set.all()
        # Perform analysis on data_points
        analysis_result = {}  # Replace with actual analysis result
        return analysis_result

class DataColumn(models.Model):
    visualization = models.ForeignKey(Visualization, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=50)

    def __str__(self):
        return self.column_name

class DataPoint(models.Model):
    visualization = models.ForeignKey(Visualization, on_delete=models.CASCADE)
    data = models.JSONField(default={})

    def __str__(self):
        return str(self.data)
