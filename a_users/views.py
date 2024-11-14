from django.shortcuts import render, redirect, get_object_or_404
from a_users.models import Profile
from django.contrib.auth.models import User
from pages import views
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def profile(request, username=None):
    return render(request, 'profile/profile.html', {'profile': profile})

@login_required
def editprofile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile.display_name = request.POST.get('display_name')
        profile.bio = request.POST.get('bio')
        if 'profile_image' in request.FILES:
            profile.image = request.FILES['profile_image']
        profile.save()
        return redirect('profile')
    return render(request, 'profile/editprofile.html')


@login_required
def settings(request):
    return render(request, 'pages/settings.html')