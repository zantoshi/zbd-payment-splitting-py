from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
import json

from .util import *
import environ

env = environ.Env()
environ.Env.read_env()
apikey = env('ZEBEDEE_API_KEY')
callback_url = env('CALLBACK_URL')


def index(request):

    return render(request, "payment_splitting/index.html")



def confirm(request):
    if request.POST:
        payload = request.POST.dict()
        request.session['amount'] = payload["amount"] + "000"
        request.session['amount_per_ln_address'] = int(round(float(payload["amount"]) / 2, 0))
        request.session['lnaddress1'] = payload["lnaddress1"]
        request.session['lnaddress2'] = payload["lnaddress2"]
        ctx = {
            'amount_per_ln_address': request.session['amount_per_ln_address'],
            'amount': payload["amount"],
            'refund_lnaddress': payload["refund_lnaddress"],
            'lnaddress1':  payload["lnaddress1"],
            'lnaddress2':  payload["lnaddress2"]
        }

    return render(request, "payment_splitting/confirm.html", ctx)

def pay(request):

    res = create_charge(apikey, request.session['amount'])
    charge = res["data"]["invoice"]["uri"]
    charge_id = res["data"]["id"]
    ctx = {
        'charge': charge,
        'charge_id': charge_id
    }


    return render(request, "payment_splitting/pay.html", ctx)


def success(request):

    return render(request, "payment_splitting/success.html")


def callback(request):
    data = json.loads(request.body)
    return HttpResponse(True)

def charge_status(request):
    charge_id = request.GET["charge_id"]
    url = f'https://api.zebedee.io/v0/charges/{charge_id}'
    heads = {'Content-Type': 'application/json', 'apikey': apikey}
    res = requests.get(url, headers=heads).json()
    paid = False
    if res["data"]["status"] == "completed":
        if not paid:
            payment = pay_to_ln_address(apikey, request.session['lnaddress1'], request.session['amount_per_ln_address'])
            payment = pay_to_ln_address(apikey, request.session['lnaddress2'], request.session['amount_per_ln_address'])
            paid = True
        resp = HttpResponse("True")
        resp.headers["HX-Redirect"] = f'success'
        return resp
    return HttpResponse("Charge has not been paid.")


def withdrawal(request):

    res = get_withdrawal(apikey)
    withdrawal = res["data"]["invoice"]["uri"]
    withdrawal_id = res["data"]["id"]
    ctx = {
        'withdrawal': withdrawal,
        'withdrawal_id': withdrawal_id
    }


    return render(request, "payment_splitting/withdrawal.html", ctx)


def withdrawal_status(request):
    withdrawal_id = request.GET["withdrawal_id"]
    url = f'https://api.zebedee.io/v0/withdrawal-requests/{withdrawal_id}'
    heads = {'Content-Type': 'application/json', 'apikey': apikey}
    res = requests.get(url, headers=heads).json()
    if res["data"]["status"] == "completed":
        resp = HttpResponse("True")
        resp.headers["HX-Redirect"] = f'success'
        return resp
    return HttpResponse("Withdrawal has not been completed.")



# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'