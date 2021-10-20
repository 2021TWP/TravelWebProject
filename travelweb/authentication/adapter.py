from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_redirect_url(self, request):
        path = 'http://localhost:3000/authentication/emailconfirmed/'
        return path

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.name = data.get('name')
        user.save()
        return user
