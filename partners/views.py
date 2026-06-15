from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ServiceProvider

def register(request):
    if request.method == "POST":
        try:
            full_name = request.POST.get('full_name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            service = request.POST.get('service')
            experience = request.POST.get('experience')
            address = request.POST.get('address')

            profile_picture = request.FILES.get('profile_picture')
            id_proof = request.FILES.get('id_proof')

            # Basic Validation
            if not all([full_name, phone, email, service, experience, address]):
                messages.error(request, "সবগুলো ফিল্ড পূরণ করুন!")
                return redirect('provider_register')

            if not profile_picture or not id_proof:
                messages.error(request, "Profile Picture এবং ID Proof আপলোড করা আবশ্যক!")
                return redirect('provider_register')

            # Create Provider
            ServiceProvider.objects.create(
                full_name=full_name,
                phone=phone,
                email=email,
                service=service,
                experience=experience,
                address=address,
                profile_picture=profile_picture,
                id_proof=id_proof,
                status='pending'   # Admin will approve later
            )

            messages.success(request, "আপনার রেজিস্ট্রেশন সফল হয়েছে! অ্যাডমিন আপনার আবেদন রিভিউ করবে।")
            return redirect('home')   # or 'provider_register'

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('provider_register')

    return render(request, 'provider-register.html')