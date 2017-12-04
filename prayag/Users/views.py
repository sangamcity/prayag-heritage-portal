from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages  
from Users.forms import SignUpForm
from django.contrib.auth.decorators import login_required
# def signup(request):
# 	return render(request, 'signup.html', {})


def signup(request):
    if request.method == 'POST': 
        form = SignUpForm(request.POST)  
        if not form.is_valid():
            print('form invalid')
            return render(request, 'signup.html',{
              'signup_form': form,  
              }) 
  
        else:
            print('saving user')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # gender = form.cleaned_data.get('gender')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            User.objects.create_user(username=username, password=password)  # removed email at signup to make signup fast
            user = authenticate(username=username, password=password)           


            # user.profile.gender = gender
            user.last_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            # messages.add_message(request,
            #                      messages.SUCCESS,
            #                      'Welcome '+user.username+'\n'
                                 # )

            return redirect('home')

    else: 
        print('method is not post')
        return render(request, 'signup.html',{
          'signup_form': SignUpForm(),
          })

def signin(request):
	return render(request, 'signin.html', {})


@login_required 
def settings(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileFormHuman(request.POST)
        if form.is_valid():
            # csrf_token = form.cleaned_data.get('_token');
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Your profile was successfully edited.')

    else:
        form = ProfileFormHuman(instance=user, initial={
            'email' : user.email,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            })
    return render(request, 'settings.html', {'form': form, 'page_user':user})

@login_required
def password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 'Your password was successfully changed.')
            return redirect('password')

    else:
        form = ChangePasswordForm(instance=user)

    return render(request, 'password.html', {'form': form, 'page_user':user})
