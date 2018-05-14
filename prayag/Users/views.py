from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages  
from Users.forms import SignUpForm, ChangePasswordForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.core.mail import send_mail
from TourismPlaces.models import TourismPlace, Review
# def signup(request):
#   return render(request, 'signup.html', {})



@login_required 
def profile(request):
    # likers = User.objects.all.filter()
    user = request.user
    if request.method == 'POST':
        # form = ProfileEditForm(request.POST)
        # if form.is_valid():
        #     # csrf_token = form.cleaned_data.get('_token');
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        messages.add_message(request,
                             messages.SUCCESS,
                                 'Your profile was successfully edited.')

    # else:
    #     form = ProfileEditForm(instance=user, initial={
    #         'email' : user.email,
    #         'first_name' : user.first_name,
    #         'last_name' : user.last_name,
    #         })
    return render(request, 'profile.html', {'page_user':user})
     
def signup(request):
    print('inside signup, Users.view') 
    if request.method == 'POST':
        error = True 
        form = SignUpForm(request.POST)
        if not form.is_valid():
            print('invalid form')
            print(form)
            return render(request, 'signup.html',{ 'form': SignUpForm(), 'error':error}) 
    
        else:  
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            User.objects.create_user(username=username, password=password, email=email)  # removed email at signup to make signup fast
            user = authenticate(username=username, password=password)           

            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Welcome in Prayag! Ready to get surprosed by Wonders in Prayag!.')
            return redirect('home')

    else: 
        return render(request, 'signup.html',{
          'form': SignUpForm(),
          })


def login_cancelled(request):
    return redirect('signin')

# @login_required 
# def settings(request):
#     user = request.user
#     if request.method == 'POST':
#         form = ProfileFormHuman(request.POST)
#         if form.is_valid():
#             # csrf_token = form.cleaned_data.get('_token');
#             user.first_name = form.cleaned_data.get('first_name')
#             user.last_name = form.cleaned_data.get('last_name')
#             user.save()
#             messages.add_message(request,
#                                  messages.SUCCESS,
#                                  'Your profile was successfully edited.')

#     else:
#         form = ProfileFormHuman(instance=user, initial={
#             'email' : user.email,
#             'first_name' : user.first_name,
#             'last_name' : user.last_name,
#             })
#     return render(request, 'settings.html', {'form': form, 'page_user':user})

@login_required
def change_password(request):
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
            return redirect('home')

    else:
        form = ChangePasswordForm(instance=user)

    return render(request, 'change_password.html', {'form': form, 'page_user':user})

@login_required(login_url='/login/')
def post_review(request):
    print('came inside')
    user = request.user
    message = request.POST.get('message')
    place_slug = request.POST.get('place_slug')
    tourism_place = get_object_or_404(TourismPlace, slug=place_slug)
    message = message.strip()
    review = Review()
    review.user = user
    review.tourism_place = tourism_place
    review.post = message[:255]
    review.save()
    print('saved review')
    messages.add_message(request, messages.SUCCESS,
                                'Your Review successfully saved.')    
    print('redirecting')
    # return redirect('home')
    return redirect('/place_detail/%s'%(place_slug))

def feedback(request):
    if request.method == 'POST': 
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        message = email + " " + message
        subject = "Prayag protal"
        from_mail = settings.EMAIL_HOST_USER
        to_mail = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_mail, to_mail, fail_silently = False)
        message_to_user = 'We have successfully received your feedback. We are happy to see'\
                          + ' you on the portal. Please tell us again if you have some suggestions or complainta'\
                          + ' about anything on the portal.\n'\
                          + 'May you have an awesome day, ahead!\n'\
                          + ' Allahabad Administration http://prayagtourism.hohos.in'
        user_email = [email]
        subject_to_user = 'Thanks for your feedback @prayagtourism'
        send_mail(subject_to_user, message_to_user, from_mail, user_email, fail_silently = False)        
        messages.add_message(request, messages.SUCCESS,
                             'Your review was successfully received.')
    else: return render(request, 'feedback.html', {})
    return redirect('feedback')


