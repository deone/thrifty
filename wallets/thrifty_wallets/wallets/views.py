from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from .models import Wallet

def get_post_data(dct):
    return (dct['id'], dct['amount'])

def perform_action(wallet_id, amount, action):
    try:
        wallet = Wallet.objects.get(pk=wallet_id)
    except Wallet.DoesNotExist:
        return {'code': 404, 'message': 'Wallet does not exist.'}
    else:
        if action == 'topup':
            wallet.balance = wallet.balance + int(amount)
        elif action == 'pay':
            wallet.balance = wallet.balance - int(amount)

        wallet.save()
        return {'code': 200, 'value': wallet.balance}

@csrf_protect
@ensure_csrf_cookie
def get(request, phone_number):
    response = {}

    try:
        wallet = Wallet.objects.get(phone_number=phone_number)
    except Wallet.DoesNotExist:
        response.update({'code': 404, 'message': 'Wallet does not exist.'})
    else:
        response.update({
          'code': 200,
          'value': wallet.to_dict()
        })

    return JsonResponse(response)

@csrf_protect
@ensure_csrf_cookie
def topup(request):
    response = {}

    if request.method == 'POST':
        wallet_id, amount = get_post_data(request.POST)
        response.update(perform_action(wallet_id, amount, 'topup'))
    else:
        response.update({'status': 'ok'})

    return JsonResponse(response)

@csrf_protect
@ensure_csrf_cookie
def pay(request):
    response = {}

    if request.method == 'POST':
        wallet_id, amount = get_post_data(request.POST)
        response.update(perform_action(wallet_id, amount, 'pay'))
    else:
        response.update({'status': 'ok'})

    return JsonResponse(response)
