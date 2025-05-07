from django.shortcuts import render

def members(request):
    return render(request, 'table.html')  # or your actual template name
