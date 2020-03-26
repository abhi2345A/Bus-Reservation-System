from django.shortcuts import render, redirect
from .forms import UserForm, RegistrationForm, LoginForm, SelectionForm
from django.http import HttpResponse, Http404
from selection.models import Passenger, Room
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home.html')

@login_required
def reset(request):
    r = Room.objects.all()
    p = Passenger.objects.all()
    return render(request,'resetdetails.html',{'r': r,'p':p})

@login_required
def Clear(request):
    if request.method =='GET':
        default = True
        for room in Room.objects.all():
            room.vacant = default
            room.save()
        for passenger in Passenger.objects.all():
            passenger.seat = None
            passenger.seat_allotted = False
            passenger.save()

        #return render(request,'resetdetails',{'r1':r1,'p1':p1})
    messages.info(request, 'All Bus Tickets have been reset(Opened) successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def Showtable(request):
    query_results = Passenger.objects.all()
    return render(request,'display.html',{'query_results': query_results})

@login_required
def ShowopenSeats(request):
    qr = Room.objects.all()
    return render(request,'openseats.html',{'qr':qr})

@login_required
def ShowClosedSeats(request):
    qr1 = Room.objects.all()
    return render(request,'closedseats.html',{'qr1':qr1})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            Passenger.objects.create(user=new_user)
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login/edit/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
        else:
            messages.error(request,"Something Went Wrong!...Try Again")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserForm()
        args = {'form': form}
        return render(request, 'reg_form.html', args)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    passenger = request.user.passenger
                    return render(request, 'profile.html', {'passenger': passenger})
                else:
                    return HttpResponse('Disabled account')
            else:
                messages.error(request,"Invalid username or password!...Try Again ")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request,"Invalid username or password!...Try Again ")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def warden_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if not user.is_warden:
                    return HttpResponse('Invalid Login')
                elif user.is_active:
                    login(request, user)
                    room_list = request.user.warden.hostel.room_set.all()
                    context = {'rooms': room_list}
                    return render(request, 'warden.html', context)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def edit(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, instance=request.user.passenger)
        if form.is_valid():
            form.save()
            passenger = request.user.passenger
            return render(request, 'profile.html', {'passenger': passenger})
        else:
            return HttpResponse(form.errors)
    else:
        form = RegistrationForm(instance=request.user.passenger)
        return render(request, 'edit.html', {'form': form})


@login_required
def select(request):
    if request.user.passenger.seat:
        seat_id_old = request.user.passenger.seat_id

    if request.method == 'POST':
        form = SelectionForm(request.POST, instance=request.user.passenger)
        if form.is_valid():
            if request.user.passenger.seat_id:
                request.user.passenger.seat_allotted = True
                r_id_after = request.user.passenger.seat_id
                seat = Room.objects.get(id=r_id_after)
                seat.vacant = False
                seat.save()
                try:
                    seat = Room.objects.get(id=seat_id_old)
                    seat.vacant = True
                    seat.save()
                except BaseException:
                    pass
            else:
                request.user.passenger.seat_allotted = False
                try:
                    seat = Room.objects.get(id=seat_id_old)
                    seat.vacant = True
                    seat.save()
                except BaseException:
                    pass
            form.save()
            passenger = request.user.passenger
            return render(request, 'profile.html', {'passenger': passenger})
        else:
            messages.error(request,"This Seat Ticket is Closed!...Try different one")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = SelectionForm(instance=request.user.passenger)
        passenger_gender = request.user.passenger.gender
        x = Room.objects.none()       
        #form.fields["room"].queryset = x
        return render(request, 'select_room.html', {'form': form})
        #return HttpResponse('Yes')


def logout_view(request):
    logout(request)
    return redirect('/')





def Seat_layout(request):
    room_list = Room.objects.order_by('name')
    room_dict = {'rooms':room_list}
    return render(request, 'Seat_layout.html', context=room_dict)







