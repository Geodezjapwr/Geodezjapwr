from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Opinia
from .forms import OpiniaForm


def index(request):
    if request.method == "POST":
        form = OpiniaForm(request.POST)
        if form.is_valid():
            opinia = form.save(commit=False)
            opinia.published_date = timezone.now()
            opinia.save()
            return render(request, 'strona/bazowy.html', {'form': form})
    else:
        form = OpiniaForm()
    return render(request, 'strona/index.html', {'form': form})


