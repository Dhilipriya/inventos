from django.urls import path
from . import views
urlpatterns=[
    path('',views.landing,name='landing'),
    path('about',views.about,name='about'),
    path('watch',views.watch,name='watch'),
    path('contact',views.contact,name='contact'),
    path('login_form',views.login_form,name='login_form'),
    path('register_form',views.register_form,name='register_form'),
    path('forget_password_form',views.forget_password_form,name='forget_password_form'),
    path('index',views.index,name='index'),
    path('index2',views.index2,name='index2'),
    path('umv',views.umv,name='umv'),
    path('UMV_add',views.UMV_add,name='UMV_add'),
    path('umv_edit',views.umv_edit,name='umv_edit'),
    path('category_List',views.category_List,name='category_List'),
    path('category_add',views.category_add,name='category_add'),
    path('category_edit',views.category_edit,name='category_edit'),
    path('unitlist',views.unitlist,name='unitlist'),
    path('unitadd',views.unitadd,name='unitadd'),
    path('unitedit',views.unitedit,name='unitedit'),
    path('tax',views.tax,name='tax'),
    path('tax_Add',views.tax_Add,name='tax_Add'),
    path('tax_edit',views.tax_edit,name='tax_edit'),
    path('product_Add',views.product_Add,name='product_Add'),
    path('product_List',views.product_List,name='product_List'),
    path('product_edit',views.product_edit,name='product_edit'),
    path('quotation_List',views.quotation_List,name='quotation_List'),
    path('quotation_Add',views.quotation_Add,name='quotation_Add'),
    path('quotation_edit',views.quotation_edit,name='quotation_edit'),
    path('saleslist',views.saleslist,name='saleslist'),
    path('purchase_List',views.purchase_List,name='purchase_List'),
    path('purchase_Add',views.purchase_Add,name='purchase_Add'),
    path('purchase_edit',views.purchase_edit,name='purchase_edit'),
    path('stocktransfer_List',views.stocktransfer_List,name='stocktransfer_List'),
    path('stocktransfer_Add',views.stocktransfer_Add,name='stocktransfer_Add'),
    path('stocktransfer_edit',views.stocktransfer_edit,name='stocktransfer_edit'),
    path('returnproduct',views.returnproduct,name='returnproduct'),
    
    path('profile',views.profile,name='profile'),
   
    path('contact_form_submission',views.contact_form_submission,name='contact_form_submission'),
    path('register_form_submission',views.register_form_submission,name='register_form_submission'),
    path('login_form_submission',views.login_form_submission,name='login_form_submission'),
    path('logout',views.logout,name='logout'),
    path('add_user_form_submission',views.add_user_form_submission,name='add_user_form_submission'),





]