from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from Users.models import Profile
from prayag.settings import ALLOWED_SIGNUP_DOMAINS
import re 


def SignupDomainValidator(value):
    if '*' not in ALLOWED_SIGNUP_DOMAINS:
        try:
            domain = value[value.index("@"):]
            if domain not in ALLOWED_SIGNUP_DOMAINS:
                raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501

        except Exception:
            raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501

     
def ForbiddenUsernamesValidator(value):
    forbidden_usernames = ['admin', 'settings', 'news', 'about', 'help',
                           'signin', 'signup', 'signout', 'terms', 'privacy',
                           'cookie', 'new', 'login', 'logout', 'administrator',
                           'join', 'account', 'username', 'root', 'blog',
                           'user', 'users', 'billing', 'subscribe', 'reviews',
                           'review', 'blog', 'blogs', 'edit', 'mail', 'email',
                           'home', 'job', 'jobs', 'contribute', 'newsletter',
                           'shop', 'profile', 'register', 'auth',
                           'authentication', 'campaign', 'config', 'delete',
                           'remove', 'forum', 'forums', 'download',
                           'downloads', 'contact', 'blogs', 'feed', 'feeds',
                           'faq', 'intranet', 'log', 'registration', 'search',
                           'explore', 'rss', 'support', 'status', 'static',
                           'media', 'setting', 'css', 'js', 'follow',
                           'activity', 'questions', 'articles', 'network', ]

    if value.lower() in forbidden_usernames: 
        raise ValidationError('This is a reserved word.')


def UniquePhoneValidator(value):
    print('inside phone validation')
    if not '@' in value and not '.' in value:
        print('Its a phone')     
        phone = value
        phone_format = re.compile("^\d+")
        isnumber = re.match(phone_format,phone)
        if not isnumber or len(phone)!=10 or int(phone)<0:
            print('invalid phone')
            raise ValidationError('Enter a valid Phone Number.')


def UniqueEmailValidator(value):
    print('inside email validation')
    if '@' in value and '.' in value and User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


# def UniqueUsernameIgnoreCaseValidator(value):
#     if User.objects.filter(username__iexact=value).exists():
#         raise ValidationError('User with this Username already exists.')


class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-width', 'placeholder':'Phone or Email'}),
        label='',
        max_length=30,
        required=True,
        help_text='')  # noqa: E261
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-width', 'placeholder':'First Name'}),
        label='',
        max_length=30,
        required=True,
        help_text='')  # noqa: E261
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-width', 'placeholder':'Last Name'}),
        label='',
        max_length=30,
        required=True,
        help_text='')  # noqa: E261
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control input-width', 'placeholder':'Choose a strong Password'}),
        label='',
        )
    # confirm_password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    #     label="Confirm your password",
    #     required=True)

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'first_name', 'last_name', 'password', ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        self.fields['username'].validators.append(UniquePhoneValidator)
        self.fields['username'].validators.append(UniqueEmailValidator)
        # self.fields['email'].validators.append(UniqueEmailValidator)
        # self.fields['email'].validators.append(SignupDomainValidator)
        self.fields['password'].required = True        
        # self.fields['confirm_password'].required = True
        # self.fields['email'].required = True

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        # confirm_password = self.cleaned_data.get('confirm_password')
        if password and len(password) < 4:
            self._errors['password'] = self.error_class(
                ['Passwords too sort'])
        # if password and password != confirm_password:
        #     self._errors['password'] = self.error_class(
        #         ['Passwords don\'t match'])
        return self.cleaned_data


class ChangePasswordForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old password",
        required=True)

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New password",
        required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm new password",
        required=True)

    class Meta:
        model = User
        fields = ['id', 'old_password', 'new_password', 'confirm_password']

    def clean(self):
        super(ChangePasswordForm, self).clean()
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        id = self.cleaned_data.get('id')
        user = User.objects.get(pk=id)
        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class([
                'Old password don\'t match'])
        if new_password and len(new_password) < 4:
            self._errors['new_password'] = self.error_class(
                ['Passwords too sort'])
        if new_password and new_password != confirm_password:
            self._errors['new_password'] = self.error_class([
                'Passwords don\'t match'])
        return self.cleaned_data

 

class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30, 
        required=False)
    email = forms.CharField( 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=100,
        required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'email']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].validators.append(UniqueEmailValidator)
        self.fields['email'].validators.append(SignupDomainValidator)