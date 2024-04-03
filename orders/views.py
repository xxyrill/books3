import stripe   # for charge view
from django.conf import settings
from django.contrib.auth.models import Permission # for book access after making purchase
from django.views.generic.base import TemplateView
from django.shortcuts import render # for charge view

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY    # for charge view

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    # get the permission
    permission = Permission.objects.get(codename='special_status')

    # get user
    u = request.user

    # add to user's permission set
    u.user_permissions.add(permission)

    # to render page after making purchase
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken'],
        )
        return render(request, 'orders/charge.html') # this will render charge.html after purchase
