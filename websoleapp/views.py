from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import ContactForm

# def contact_form_submit(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['complete_name']
#             email = form.cleaned_data['email_address']
#             phone = form.cleaned_data['phone_no']
#             method = form.cleaned_data['preferred_method']

#             # Sending email to admin
#             subject = "New Contact Form Submission"
#             message = f"""
#             Name: {name}
#             Email: {email}
#             Phone: {phone}
#             Preferred Method: {method}
#             """
#             admin_email = "parasharankurdbg@gmail.com"  # Replace with admin email
#             send_mail(subject, message, email, [admin_email])

#             return JsonResponse({"status": "success", "message": "Your request has been submitted successfully."})
#         else:
#             return JsonResponse({"status": "error", "message": "Invalid form data."})
#     return JsonResponse({"status": "error", "message": "Invalid request."})
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.http import JsonResponse
from .forms import ContactForm
from django.conf import settings

def contact_form_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            name = form.cleaned_data['complete_name']
            email = form.cleaned_data['email_address']
            phone = form.cleaned_data['phone_no']
            company = form.cleaned_data['company_name']
            requirements = form.cleaned_data['requirements']
            file_upload = form.cleaned_data.get('file_upload')  # Get the file if it exists
            image_upload = form.cleaned_data.get('image_upload')  # Get the image if it exists

            # Construct the email message
            subject = "New Contact Form Submission"
            message = f"""
            Name: {name}
            Email: {email}
            Phone: {phone}
            Company: {company}
            Requirements: {requirements}
            """

            # Send email with file attachment
            admin_email = "parasharankurdbg@gmail.com"  # Replace with admin email
            email_message = EmailMessage(subject, message, email, [admin_email])

            # Attach files if they exist
            if file_upload:
                email_message.attach(file_upload.name, file_upload.read(), file_upload.content_type)
            if image_upload:
                email_message.attach(image_upload.name, image_upload.read(), image_upload.content_type)

            # Send email
            email_message.send()

            return JsonResponse({"status": "success", "message": "Your request has been submitted successfully."})
        else:
            return JsonResponse({"status": "error", "message": "Invalid form data."})

    return JsonResponse({"status": "error", "message": "Invalid request."})

# def comming_soon(request):
#     return render(request,'comming_soon.html')

def about_us(request):
    return render(request,'about.html')

# def testimonials(request):
#     return render(request, 'testimonials.html')

