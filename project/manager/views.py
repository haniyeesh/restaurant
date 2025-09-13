
from django.shortcuts import render,redirect
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseForbidden
from account.models import Manager_permission
from home.models import Reservations


def manager(request):
    manage = Manager_permission.objects.all()
    return render(request, 'manage.html', {'manage' :manage})

def reserve_status(request, reservation_id):
    reservation = get_object_or_404(Reservations, id=reservation_id)
    new_status = request.POST.get('status')
    if new_status not in ['pending', 'confirmed', 'canceled']:
        return HttpResponseForbidden("وضعیت نامعتبر است.")
    reservation.status = new_status
    reservation.save()

    return redirect('reserve')

def table(request):
    reservations = Reservations.objects.all()
    return render(request, 'tables.html', {'reservations':reservations})