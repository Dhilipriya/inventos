
from django.shortcuts import render
from .models import contact_table, reg_table,add_user
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def landing(request):
    return render(request,'landing.html')

def about(request):
    return render(request,'about.html')

def watch(request):
    return render(request,'watch.html')
    
def contact(request):
    return render(request,'contact.html')

def contact_form_submission(request):
    if request.method=="POST":
        ex1=contact_table(name=request.POST.get('name'),
                          email=request.POST.get('email'),
                          phone_number=request.POST.get('phone_number'),
                          message=request.POST.get('message'))
        ex1.save()
        messages.error(request,'sucessfully sent..!!!')
        print("inside")
        return render(request,'contact.html')
    else:
        print("outside")
        return render(request,'contact.html')

        
def login_form(request):
    return render(request,'login_form.html')
                                        
def login_form_submission(request):
    if reg_table.objects.filter(email_id=request.POST['email_id'],password=request.POST['password']).exists():
        print("logged in")
        ex1=reg_table.objects.get(email_id=request.POST['email_id'],password=request.POST['password'])
        take_username=ex1.user_name
        take_emailid=ex1.email_id

        print("user_name:",take_username)
        print("email_id:",take_emailid)
        logger_data=reg_table.objects.get(email_id=take_emailid)
        return render(request,'index.html',{'logger_data':logger_data})
    else:    
        print("failed to login")
        messages.error(request,'user_name or password invaild..!!',extra_tags='failed_to_login')
        return render(request,'login.html') 
def logout(request):
    auth.logout(request)
    return render(request,'login_form.html')         
                                                                 
def register_form(request):
    return render(request,'register_form.html')
                                                                                                   
def register_form_submission(request):
    if request.method=="POST":
         ex1=reg_table(email_id=request.POST.get('email_id'),
         user_name=request.POST.get('user_name'),
         password=request.POST.get('password'),
         confirm_password=request.POST.get('confirm_password'))
         ex1.save()
         messages.error(request,'sucessfully registered..!!!',extra_tags="register")
         print("inside")
         return render(request,'login_form.html')
    else:
        print("outside")
        return render(request,'register_form.html')


def forget_password_form(request):
    return render(request,'forget_password_form.html')

def index(request):
    return render(request,'index.html')

def index2(request):
    return render(request,'index2.html')

def umv(request):
    return render(request,'umv.html')

def UMV_add(request):
    return render(request,'UMV_add.html')

def add_user_form_submission(request):
    if request.method=="POST":
         ex1=add_user(email_id=request.POST.get('email_id'),
                      name=request.POST.get('name'),
                      group=request.POST.get('group'))
         ex1.save()
         return render(request,'umv.html')
    else:
        return render(request,'UMV_add.html')


def umv_edit(request):
    return render(request,'umv_edit.html')

def category_List(request):
    return render(request,'category_List.html')

def category_add(request):
    return render(request,'category_add.html')

def category_edit(request):
    return render(request,'category_edit.html')

def unitlist(request):
    return render(request,'unitlist.html')

def unitadd(request):
    return render(request,'unitadd.html')

def unitedit(request):
    return render(request,'unitedit.html')

def tax(request):
    return render(request,'tax.html')

def tax_Add(request):
    return render(request,'tax_Add.html') 

def tax_edit(request):
    return render(request,'tax_edit.html')

def product_List(request):
    return render(request,'product_List.html')

def product_Add(request):
    return render(request,'product_Add.html')

def product_edit(request):
    return render(request,'product_edit.html')

def quotation_List(request):
    return render(request,'quotation_List.html')

def quotation_Add(request):
    return render(request,'quotation_Add.html')

def quotation_edit(request):
    return render(request,'quotation_edit.html')

def saleslist(request):
    return render(request,'saleslist.html')

def purchase_List(request):
    return render(request,'purchase_List.html')

def purchase_Add(request):
    return render(request,'purchase_Add.html')

def purchase_edit(request):
    return render(request,'purchase_edit.html')

def stocktransfer_List(request):
    return render(request,'stocktransfer_List.html')

def stocktransfer_Add(request):
    return render(request,'stocktransfer_Add.html')

def stocktransfer_edit(request):
    return render(request,'stocktransfer_edit.html')

def returnproduct(request):
    return render(request,'returnproduct.html')


def profile(request):
    return render(request,'profile.html')
               

                                                        