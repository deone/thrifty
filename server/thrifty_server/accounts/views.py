from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from .helpers import send_request
from .models import Account

@csrf_protect
@ensure_csrf_cookie
def create(request):
    response = {}

    if request.method == 'POST':
        number = request.POST['phone_number']
        url = settings.WALLETS_URL + '%s/' % number
        data = {'phone_number': number}
        response = send_request(url, data)
        if response['code'] == 200:
            first_name = response['value']['first_name']
            last_name = response['value']['last_name']
            account = Account.objects.create(phone_number=number, first_name=first_name, last_name=last_name)
            response.update({'code': 200, 'value': account.pk})
        else:
            response.update({'code': '404', 'message': 'Wallet not found for this number.'})
    else:
        response.update({'status': 'ok'})

    return JsonResponse(response)
