from django.shortcuts import render
import os
import pandas as pd
import numpy as np

# Create your views here.
def index(request):
    dados = pd.read_csv("dashboard/out.csv", encoding="utf-8")
    json = dados.to_json(orient = "records")
    return render(request, "dashboard/index.html", {"dados": json})