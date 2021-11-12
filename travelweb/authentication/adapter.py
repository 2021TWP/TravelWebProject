from allauth.account.adapter import DefaultAccountAdapter

from travelweb import settings


class CustomAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_redirect_url(self, request):
        path = 'http://localhost:3000/authentication/emailconfirmed/'
        return path

    def get_email_confirmation_url(self, request, emailconfirmation):
        return f'http://localhost:3000/authentication/emailconfirmed/{emailconfirmation.key}/'

    def send_mail(self, template_prefix, email, context):
        msg = self.render_mail(template_prefix, email, context)
        msg.send()

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.name = data.get('name')
        user.save()
        return user
