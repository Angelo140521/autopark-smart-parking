from django.shortcuts import render
from .models import Sensor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor
from .serializers import SensorSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

from django.contrib.auth.decorators import user_passes_test
from django.db.models import Sum
from .models import ParkingHistory
from django.shortcuts import render

def admin_login_page(request):
    return render(request, 'parking/adminlogin.html')
def admin_report_page(request):
    return render(request, 'parking/adminreport.html')

def admin_report(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    histories = ParkingHistory.objects.all().order_by('-datetime')
    totals_by_date = (
        ParkingHistory.objects
        .values('datetime__date')
        .annotate(total=Sum('total_cost'))
        .order_by('-datetime__date')
    )
    return render(request, 'parking/admin_report.html', {
        'histories': histories,
        'totals_by_date': totals_by_date
    })

from .models import ParkingHistory
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def payment_page(request):
    if request.method == 'POST':
        slot = request.POST.get('slot')
        time_used = request.POST.get('time_used')
        parking_fee = int(request.POST.get('parking_fee'))
        total_cost = int(request.POST.get('total_cost'))

        ParkingHistory.objects.create(
            user=request.user,
            slot_number=slot,
            time_used=time_used,
            parking_fee=parking_fee,
            total_cost=total_cost
        )

        return redirect('dashboard')

    return render(request, 'parking/payment.html')



def history_page(request):
    return render(request, 'history.html')
def payment_page(request):
    return render(request, 'payment.html')
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'parking/signup.html', {'form': form})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    from .models import Sensor
    slots = Sensor.objects.all().order_by('slot_number')
    return render(request, 'parking/dashboard.html', {'slots': slots})


@api_view(['GET'])
def get_parking_status(request):
    sensors = Sensor.objects.all().order_by('slot_number')
    serializer = SensorSerializer(sensors, many=True)
    return Response(serializer.data)


def dashboard(request):
    slots = Sensor.objects.all().order_by('slot_number')
    return render(request, 'parking/dashboard.html', {'slots': slots})
