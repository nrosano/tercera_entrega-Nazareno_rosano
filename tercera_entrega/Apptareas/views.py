from django.shortcuts import render

def home(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)


# Create your views here.
