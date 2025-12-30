from django.shortcuts import render, redirect, get_object_or_404
from .models import Course , UserProfile

# ================= HOME =================
def home(request) :
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

# ================= COURSE DETAIL =================
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

# ================= SIGN IN =================
def signin(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        try:
            user = UserProfile.objects.get(phone=phone, password=password)
            request.session['user'] = user.id
            return redirect('home')
        except UserProfile.DoesNotExist:
            return render(request, 'signin.html', {'error': 'Invalid credentials'})

    return render(request, 'signin.html')

# ================= SIGN UP =================
def signup(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if UserProfile.objects.filter(phone=phone).exists():
            return render(request, 'signup.html', {'error': 'Phone already exists'})

        UserProfile.objects.create(phone=phone, password=password)
        return redirect('signin')

    return render(request, 'signup.html')

# ================= CART =================
def cart_view(request):
    cart = request.session.get('cart', [])
    courses = Course.objects.filter(id__in=cart)
    return render(request, 'cart.html', {'courses': courses})

def add_to_cart(request, course_id):
    cart = request.session.get('cart', [])
    if course_id not in cart:
        cart.append(course_id)
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, course_id):
    cart = request.session.get('cart', [])
    if course_id in cart:
        cart.remove(course_id)
    request.session['cart'] = cart
    return redirect('cart')

# ================= GOOGLE LOGIN =================
def google_login(request):
    return redirect('signin')
