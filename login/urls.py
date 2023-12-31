from django.urls import path,include
from . import views

urlpatterns = [
     path('',views.home,name='home'),
    # path('',views.guest_user,name='guest_user'),
    path('login',views.userlogin,name='login'),
    path('register/',views.register,name='register'),
    path('otp_login/',views.otp_login,name='otp_login'),
    path('otp_confirm/',views.otp_confirm,name='otp_confirm'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('view_product/<int:id>',views.view_product,name='view_product'),
    path('cartview', views.cartview, name='shop'),
    path('add_cart/<int:id>', views.add_cart, name='shop'), 
    path('add_cart_product_view/<int:id>', views.add_cart_product_view, name='add_cart_product_view'),
    path('increment_cart_quantity/<int:quantity>/<int:id>', views.increment_cart_quantity, name='increment_cart_quantity'),
    path('decrement_cart_quantity/<int:quantity>/<int:id>', views.decrement_cart_quantity, name='decrement_cart_quantity'),
    path('update_quantity/<int:id>', views.update_quantity, name='minus_cart_quantity'),
    
    path('delete_product_cart/<int:id>', views.delete_product_cart, name='delete_product_cart'), 
    path('delete_cart', views.delete_cart, name='delete_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('add_address/',views.add_address,name='add_address'),
    path('userprofile/',views.userprofile,name='userprofile'),
    path('choose_address/',views.choose_address,name='choose_address'),
    path('choose_payment_method/<int:id>',views.choose_payment_method,name="choose_payment_method"),
    path('choose_payment/',views.choose_payment,name='choose_payment'),
    path('payment_success_page',views.payment_success_page,name='payment_success_page'),
    path('update_address/<int:id>',views.update_address,name='update_address'),
    path('create_order/<int:id>',views.create_order,name='create_order'),
    path('order_user/',views.order_user,name='order_user'),
    # path('guest_cart/',views.guest_cart,name='guest_cart'),
    # path('guest_add_cart/', views.guest_add_cart, name='guest_add_cart'), 
    path('razorpay_pay<int:amount>/',views.razorpay_pay,name='razorpay_pay'),
    path('active_orders/',views.active_orders,name='active_orders'),
    path('razorpay_success/',views.razorpay_success,name='razorpay_success'),
    path('paypal<int:amount>/',views.paypal,name='paypal'),
    path('paypalsuccess/',views.paypalsuccess,name='paypalsuccess'),
    path('active_order_products/<int:id>',views.active_order_products,name='active_order_products'),
    path('order_products/<int:id>',views.order_products,name='order_products'),
    path('order_cancel_user/<int:id>',views.order_cancel_user,name='order_cancel_user'),
    path('delivered_orders/',views.delivered_orders,name='delivered_orders'),
    path('choose_address_select',views.choose_address_select,name='choose_address_select'),
    path('apply_coupon/<int:id>',views.apply_coupon,name='apply_coupon'),
    path('wallet/',views.wallet,name='wallet'),
    path('return_order/<int:id>',views.return_order,name='return_order')
]
