from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import Election, Candidate, Vote
from . forms import RegistrationForm, LoginForm
from django.contrib import messages

def home(request):
    elections = Election.objects.all()
    return render(request, 'home.html', {'election': elections})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def vote(request, election_id):
    election = get_object_or_404(Election, id=election_id)
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        candidate = get_object_or_404(Candidate, id=candidate_id)
        if not Vote.objects.filter(user=request.user, election=election).exists():
            Vote.objects.create(user=request.user, candidate=candidate, election=election)
            return redirect('home')
    candidates = election.candidates.all()
    return render(request, 'vote.html', {'election': election, 'candidates': candidates})
