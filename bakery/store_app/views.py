# Create your views here.

from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User , auth 

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views.decorators.csrf import csrf_protect
# from store_app.decorators import admin_required

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.views import View

from .models import * 
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponse,JsonResponse
from .forms import ReviewForm
from .forms import *
from django.contrib.auth.forms import PasswordResetForm,AuthenticationForm,PasswordResetForm,PasswordChangeForm

from django.conf import settings
from django.core.mail import send_mail

from cart.context_processor import cart_total_amount 

from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.db.models import Avg
from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt

import razorpay

client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))


#from .models import Registration






def base(request):

    itm = Item.objects.all()

    return render(request,'base.html',{'itm': itm})

def hf(request):
    return render(request,'hf.html')



def item(request):
   
    categories=Categories.objects.all()
    filter_price=Filter_Price.objects.all()
    flavour=Flavour.objects.all()

    

    CATID=request.GET.get('categories')
    PRICE_FILTER_ID=request.GET.get('filter_price')
    FLAVOURID =request.GET.get('flavour')

    ATOZID=request.GET.get('ATOZ')
    ZTOAID=request.GET.get('ZTOA')

    PRICE_LOWTOHIGHID=request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOWID=request.GET.get('PRICE_HIGHTOLOW')

    WITHEGGID=request.GET.get('WITHEGG')
    WITHOUTEGGID=request.GET.get('WITHOUTEGG')

    if CATID:
        itm = Item.objects.filter(categories=CATID,status='Publish')
    
    elif PRICE_FILTER_ID:
        itm=Item.objects.filter(filter_price=PRICE_FILTER_ID,status='Publish')

    elif ATOZID:
        itm= Item.objects.filter(status='Publish').order_by('name') 
    elif ZTOAID:
        itm= Item.objects.filter(status='Publish').order_by('-name')  


    elif PRICE_LOWTOHIGHID:
        itm= Item.objects.filter(status='Publish').order_by('price')
    elif PRICE_HIGHTOLOWID:  
        itm= Item.objects.filter(status='Publish').order_by('-price')  

    elif WITHEGGID:
        itm= Item.objects.filter(status='Publish',ingredients='WITH EGG')
    elif WITHOUTEGGID:
        itm= Item.objects.filter(status='Publish',ingredients='WITHOUT EGG')
    elif FLAVOURID:
        itm = Item.objects.filter(flavour=FLAVOURID,status='Publish')  

    else:
        itm = Item.objects.filter(status='Publish')

    context={
        'itm': itm ,
        'categories': categories ,
        'filter_price' : filter_price,
        'flavour': flavour,
    }    

    return render(request,'item.html',context)

def category(request):
    itm = Item.objects.all()
    return render(request,'category.html',{'itm': itm})

def home(request):
    return render(request,'home.html')

def gallary(request):
    return render(request,'gallary.html')

def about(request):
    return render(request,'about.html')

def Contact_Page(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        contact=Contact_us(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )

        phone = phone
        message = message
        email_from = settings.EMAIL_HOST_USER
        #try:
        send_mail(phone,message,email_from,['diyagohel3@gmail.com'])
        contact.save()
        return redirect('home')
        #except:
         #   return redirect('contact')
        
    return render(request,'contact.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        print(f"Username: {username}, Password: {password}")
       
        user = authenticate(request, username=username, password=password)
        print(f"Authenticated user: {user}")

        if user is not None :
            auth.login(request, user)
            messages.success(request, 'Login Successfull')
            if user.is_superuser:
                return redirect(settings.ADMIN_URL_PREFIX)  # Redirect admin to admin panel
            else:
                return redirect("home")    
        else: 
            messages.error(request, 'invalid credentials')
            return redirect('login') 
    else:       
        return render(request,'login.html')
        

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gender=request.POST['gender']
        username=request.POST['username']
        email=request.POST['email']
        address=request.POST['address']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:    
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User Created..')
                return redirect('login')

        else:
            print('password not matching..') 
            return redirect('register')   
        return redirect('')

    else:
       return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('home')



def search(request):
    query = request.GET.get('query')
    itm = Item.objects.filter(name__icontains = query)

    context = {
        'itm':itm
    }

    return render(request, 'search.html', context)


def product_details(request,id):
    it = Item.objects.filter(id=id).first()
    #wishlist_item_ids=Wishlist.objects.filter(user=request.user).values_list('item_id',flat=True)
    reviews = Review.objects.filter(item=it)#[:4]

    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    context = {
        'it':it,
        'reviews': reviews,
        'average_rating': average_rating,
        #'wishlist_item_ids' : wishlist_item_ids
    }
    return render(request,'product_single.html',context)




# cart start
@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("item")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'Cart/cart_detail.html')

def add_review(request, id):
    try:
        item= get_object_or_404(Item,id=id)
        user=request.user


        review_text = request.POST.get('review', '')  # Get review text from POST data
        rating_str = request.POST.get('rating', '')  


    # Validate rating: check if it's a valid integer
        try:
            rating = int(rating_str)
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5.")
        except ValueError:
            rating = 1  # Default rating to 1 if not a valid integer 

        review=Review.objects.create(
            user=user,
            item=item,
            review=review_text,
            rating=rating,
        )
        """
        original_reviews = Review.objects.filter(item=item)
        average_rating = original_reviews.aggregate(Avg('rating'))['rating__avg']
       """
        average_rating = Review.objects.filter(item=item).aggregate(Avg('rating'))['rating__avg']


        context={
        'user':user.username,
        'review':review_text,
        'rating':rating,
        'average_rating': average_rating,
        }

        # Fetch original customer review
    

        #average_reviews =Review.objects.filter(item =it) .aggregate(rating=Average ("rating"))
        return redirect('home')
        #return JsonResponse(
            #{
            #'success':True,
            #'context' : context,
            #'average_reviews' : average_reviews
            #}
        #)

    except Item.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Item does not exist.',
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e),
        })

#Wishlist

@login_required
def add_to_wishlist(request, item_id):
    if request.method == 'POST':
        
        Wishlist.objects.create(user=request.user, item_id=item_id)
        return redirect('home')
        #return JsonResponse({'success': True})
    else:
            return JsonResponse({'success': False})

@login_required
def remove_from_wishlist(request, item_id):
    if request.method == 'POST':
        
        Wishlist.objects.filter(user=request.user, item_id=item_id).delete()
        return redirect('home')
        #return JsonResponse({'success': True})
    else:
            return JsonResponse({'success': False, 'message': 'Invalid request method'})
    
def wishlist(request):
    # Retrieve wishlist items for the current user
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})# Replace this with the appropriate key value
 






def cart_view(request):
    cart = Cart(request)
    original_total = cart_total_amount(request).get('cart_total_amount',0)  # Assuming cart has a total_price attribute
    coupon_discount_percentage = 0
    discount_amount = 0
    discounted_total = original_total


    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            coupon = Coupon.objects.get(code=code, active=True)
            if coupon.valid_from <= timezone.now().date() <= coupon.valid_to:
                coupon_discount_percentage = coupon.discount_percentage
                discount_amount = (original_total * coupon_discount_percentage) / 100.0
                discounted_total = original_total - discount_amount
            else:
                discount_amount = 0
                discounted_total = original_total
        except Coupon.DoesNotExist:
            discount_amount = 0
            discounted_total = original_total

    context = {
        'cart': cart,
        'original_total': original_total,
        'coupon_discount_percentage': coupon_discount_percentage,
        'discount_amount': discount_amount,
        'discounted_total': discounted_total,
    }
    return render(request, 'Cart/cart_detail.html', context)






def Check_out(request):
    
    if request.method == "POST":
        amount_str = request.POST.get('amount',None)

    # Check if amount_str is not None before converting to int
        if amount_str is  None:
            return HttpResponse({'error': 'Amount is required.'}, status=400)
        try:
                amount = float(amount_str)
        except ValueError:
                # Handle the case when 'amount_str' cannot be converted to float
                amount = 0.0
                return HttpResponse({'error': 'Invalid amount format.'}, status=400)

            # Check if the amount is less than 1.00
        if amount < 1.00:
            return HttpResponse( 'Amount must be at least $1.00.', status=400)
        # return JsonResponse({'success': 'Payment processed successfully.', 'amount': amount}, status=200)
                # Set the minimum amount to 1.00
        # amount = 1.00
    # else:
    # Provide a default value or handle the case where 'amount' is not available
        amount_in_paise = int(amount * 100 )
    #  return JsonResponse({'error': 'Invalid request method.'}, status=405)
        try:
                payment=client.order.create({
                    "amount": amount_in_paise,
                    "currency": "INR",
                    "payment_capture": True
                })
        except Exception as e:
                print(f'Payment creation failed: {str(e)}')
                return HttpResponse(f'Payment creation failed: {str(e)}', status=500)

        userprofile = Profile.objects.filter(user=request.user).first()

        order_id = payment['id']
        context={
                'order_id': order_id,
                'payment': payment,
                'userprofile':userprofile,
                'discounted_total': request.POST.get('discounted_total'),
                
        }
        
        return render(request, 'Cart/checkout.html',context)
    else:
        return HttpResponse('Invalid request method.', status=405)



def Place_Order(request):
    if request.method =="POST":

        currentuser = User.objects.filter(id =request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name=request.POST.get('firstname')
            currentuser.last_name=request.POST.get('lastname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile =Profile()
            userprofile.user =request.user
            userprofile.phone =request.POST.get('phone')
            userprofile.address=request.POST.get('address')
            userprofile.city =request.POST.get('city')
            userprofile.state=request.POST.get('state')
            userprofile.pin=request.POST.get('pin')
            userprofile.save()

        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id = uid)
        cart=request.session.get('cart')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pin=request.POST.get('pin')
        amount=request.POST.get('amount')

        order_id=request.POST.get('order_id')
        payment=request.POST.get('payment')

        context={
            'order_id':order_id,
            'discounted_total': request.POST.get('discounted_total'),
        }

        order=Order(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            pin=pin,
            payment_id=order_id,
            amount=amount,
        )
        order.save()
        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']



            total = a * b


            item=OrderItem(
                user=user,
                order=order,
                item = cart[i]['name'],
                image = cart[i]['image'],
                quantity = cart[i]['quantity'],
                price = cart[i]['price'],
                total= total
            )
            item.save()

        return render(request, 'Cart/placeorder.html',context)  





@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id=val
                break

       # Check if the order ID is not empty
        if order_id:
            # Retrieve the order object from the database
            try:

                user=Order.objects.get(payment_id = order_id)
                # Print debugging information
                print("Order ID:", user.id)  # Print the order ID for debugging
            except Order.DoesNotExist:
                return HttpResponse("Order not found.", status=404)
        
            user.paid = True
            user.save()
            messages.success(request,"Your order been placed succesfully!!")
            context = {'order': user}  # Pass the order object to the template context
            return render(request,'Cart/thank-you.html',context)
    
        else:
            return HttpResponse("Invalid order ID.")
    
    else:
    
        return HttpResponse("Invalid request method.")
        

    return render(request,'Cart/thank-you.html',context)


def Your_Order(request):
    # uid=request.session.get('_auth_user_id')
    # user=User.objects.get(id = uid)

    # orders=OrderItem.objects.all()
    user = request.user
    orders = Order.objects.filter(user=user)
    context={
        'orders':orders,

    }

    return render(request,'your_order.html',context)


# cart end





def submit_review(request, item_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            
            # Print the form data
            print("Rating:", form.cleaned_data['rating'])
            print("review:", form.cleaned_data['review'])

            # Save the instance to the database
            instance = form.save()
            
            # Print the instance data
            print("Instance Rating:", instance.rating)
            print("Instance Other Fields:", instance.review)

            return redirect('item')  # Redirect to a success page
    else:
        form = ReviewForm()

    return render(request, 'item.html', {'form': form})
"""
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST,instance=request.user)
                user = User.objects.all()
            else:                   
                fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request,'Profile Updated...!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                user = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
            context={
                'name': request.user.username,
                'form': fm,
                'user': user,
            }
        return render(request, 'profiles/profile.html',context)
    else:
        return HttpResponseRedirect('/login/')



#Wishlist
def wishlist(request):
    return render(request,'wishlist.html')

def profile_edit(request):
    return render(request,'profiles/profile_edit.html')


@login_required(login_url="/login/")
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profiles/profile.html')
    else:
        return redirect('/login/')
"""

# profile start
class ProfileView(LoginRequiredMixin, TemplateView):
   
    template_name = 'profiles/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'profiles/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            # profile = profile_form.save(commit=False)
            # profile.user = request.user  # Associate the profile with the current user
            # profile.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))
            # return redirect('profile')

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
#end profile

def generate_invoice(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return HttpResponse("Order not found.", status=404)

    template_path = 'Cart/invoice.html'
    context = {'order': order}

    # Render the template with context data
    template = get_template(template_path)
    html = template.render(context)

    # Create PDF using xhtml2pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order_id}.pdf"'

    # Generate PDF using pisa library
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error generating PDF.")

    return response


