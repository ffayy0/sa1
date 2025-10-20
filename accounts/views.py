from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile

def register_view(request):
    """عرض إنشاء حساب جديد"""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم بالفعل.")
            return redirect("accounts:register")

        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, phone=phone, address=address, city=city)
        messages.success(request, "تم إنشاء الحساب بنجاح، يمكنك تسجيل الدخول الآن.")
        return redirect("accounts:login")

    return render(request, "account_templates/register.html")


def login_view(request):
    """عرض تسجيل الدخول"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"مرحبًا بك يا {user.username} 🎉")
            return redirect("/")  # يمكنك تعديل الوجهة
        else:
            messages.error(request, "بيانات الدخول غير صحيحة.")
            return redirect("accounts:login")

    return render(request, "account_templates/login.html")


def logout_view(request):
    """تسجيل خروج المستخدم"""
    logout(request)
    messages.info(request, "تم تسجيل خروجك بنجاح 👋")
    return redirect("/")
