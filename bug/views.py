from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import BugForm
from .models import Bug 

def bug_submission(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_bugs')
    else:
        form = BugForm()

    return render(request, 'create_bug.html', {'form': form})

def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'list_bugs.html', {'bugs': bugs})

def bug_details(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    return render(request, 'bug_detail.html', {'bug':bug})
 


