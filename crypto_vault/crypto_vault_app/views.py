from django.shortcuts import render

def home(request):
    return render(request, 'crypto_vault_app/index.html')
