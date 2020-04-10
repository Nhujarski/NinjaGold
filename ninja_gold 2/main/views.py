from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
    if 'coins' not in request.session:
        request.session['coins'] = 0
    
    return render(request,'index.html')

def process_money(request):
    if 'messages' not in request.session:
        request.session['messages'] = []
    lst = request.session['messages']
    if request.POST['buildings'] == 'farm':
        coins = random.randint(10,20)
        request.session['coins'] += coins
        message = f"<p class = 'green'>Earned { coins } in farm</p>"
        lst.append(message)
    if request.POST['buildings'] == 'cave':
        coins = random.randint(5,10)
        request.session['coins'] += coins
        message = f"<p class = 'green'>Earned { coins } in cave</p>"
        lst.append(message)
    if request.POST['buildings'] == 'house':
        coins = random.randint(2,5)
        request.session['coins'] += coins
        message = f"<p class = 'green'>Earned { coins } in house</p>"
        lst.append(message)
    if request.POST['buildings'] == 'casino':
        coins = random.randint(-50,50)
        request.session['coins'] += coins
        if coins > 0:
            message = f"<p class = 'green'>Earned { coins } in casino</p>"
            lst.append(message)
        else:
            message = f"<p class = 'red'> Lost {coins} in casino</p>"
            lst.append(message)
    request.session['messages'] = lst
    return redirect('/')