from django.shortcuts import render

# Create your views here.
def get_table_booking(request):
    return render(request, "booking/table_booking.html")