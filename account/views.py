from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.contrib import messages

from posts.models import Post
# Create your views here.

User = get_user_model()

class RegisterView(View):
    template_name = 'account/register_page.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('full-name')
        date_of_birth = request.POST.get('date-of-birth')
        password = request.POST.get("password")

        # verifing if username and email are unique
        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            try:
                user = User.objects.get(email=email)

            except User.DoesNotExist:
                user = User.objects.create(username=username, email=email, name=name, date_of_birth=date_of_birth)
                user.set_password(password)
                user.save()
                messages.success(request, "User created successfully")
                return redirect('login') 

            else:
                messages.error(request, "email already taken.")
                return render(request, self.template_name)
        
        else:
            messages.error(request, "Username already taken.")
            return render(request, self.template_name)


class LoginView(View):
    template_name = 'account/login_page.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(f"username: {username}, password: {password}")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        messages.error(request, "Invalid Username or Password.")
        return render(request, self.template_name)

def logout_view(request):
    logout(request)
    return redirect('login')

def view_profile(request, user_id):
    user = User.objects.get(id=user_id)
    posts = Post.objects.filter(user=user)
    print(posts)
    context = {
        'user' : user,
        'posts' : posts,
    }
    return render(request, 'account/user_profile.html', context=context)