from django.shortcuts import render


def home(request):
    """نمایش صفحه‌ی اصلی مینیمال برای بررسی i18n."""
    return render(request, "home.html")
