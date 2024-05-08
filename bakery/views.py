from django.shortcuts import render, redirect
from bakery.models import Cake,Booking

# Create your views here.
def index(request):
    cakes = Cake.objects.all()
    return render(request, "index.html", {'cakes': cakes})


def image_upload(request):
    if request.method == 'POST':
        cake_name = request.POST.get('cake_name')
        cake_description = request.POST.get('cake_description')
        cake_price = request.POST.get('cake_price')
        cake_type = request.POST.get('cake_type')
        event = request.POST.get('event')
        cake_image = request.FILES.get('cake_image')
        # Create a new Cake object with the form data
        new_cake = Cake.objects.create(
            cake_name=cake_name,
            cake_description=cake_description,
            cake_price=cake_price,
            cake_type=cake_type,
            event=event,
            cake_image=cake_image
        )
        new_cake.save()
        return redirect('index')

    return render(request, 'image_upload.html')

def book_cake(request, cake_id):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        mobile_number = request.POST.get('mobile_number')
        payment_mode = request.POST.get('payment_mode')

        # Retrieve the selected cake
        cake = Cake.objects.get(pk=cake_id)

        # Create a new Booking object
        new_booking = Booking.objects.create(
            cake=cake,
            customer_name=customer_name,
            mobile_number=mobile_number,
            payment_mode=payment_mode
        )
        new_booking.save()
        # Redirect to a thank you page or any other page
        # return redirect('thank_you')
        # return redirect('thank_you', booking_id=new_booking.id)
        return redirect('thank_you')
    
    else:
        # Retrieve the selected cake for display
        cake = Cake.objects.get(pk=cake_id)
        return render(request, 'cake_booking.html', {'cake': cake})

def thank_you(request):
    # Retrieve the latest booking
    latest_booking = Booking.objects.latest('id')
    return render(request, 'thank_you.html', {'booking': latest_booking})