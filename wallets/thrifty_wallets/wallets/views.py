from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from .models import Wallet

@csrf_protect
@ensure_csrf_cookie
def topup(request):
    response = {}

    if request.method == 'POST':
        wallet_id = request.POST['id']
        amount = request.POST['amount']

        try:
            wallet = Wallet.objects.get(pk=wallet_id)
        except Wallet.DoesNotExist:
            response.update({'code': 404})
        else:
            wallet.balance = wallet.balance + int(amount)
            wallet.save()
            response.update({'code': 200})
    else:
        response.update({'status': 'ok'})

    return JsonResponse(response)

def pay(request):
    pass
