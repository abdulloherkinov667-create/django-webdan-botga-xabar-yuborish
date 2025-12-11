from django.shortcuts import render
import requests

TOKEN = '8509577840:AAGD_P8erKvKhjnpa6Ya5hBNinEtdQdMqok'
ADMIN_BU = '6411347321'


def botroy(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        last = request.POST.get('lastnsme')
        useremail = request.POST.get('email')

        bot_text = f"""
Yangi odamdan xabar bor:

Ismi: {name}
Familyasi: {last}
Emaili: {useremail}
"""

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": ADMIN_BU, "text": bot_text}

        requests.post(url, data=data)

    return render(request, 'botroyxa.html')
