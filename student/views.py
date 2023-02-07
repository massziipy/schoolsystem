from django.shortcuts import render

# Create your views here.


def student_home_page(request):
    return render(request,'student/student_home.html') 

def pay_fee_page(request):
    return render(request,'student/pay_fees.html') 

def view_report_card_page(request):
    return render(request,'student/view_report_card.html') 

