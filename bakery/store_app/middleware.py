# # store_app/middleware.py

# from django.conf import settings
# from django.contrib.auth import logout
# from django.shortcuts import redirect,render
# from django.contrib import messages

# class AdminAccessMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
        
#         # Check if the user is authenticated and is accessing customer pages
#         if request.user.is_authenticated and not request.user.is_superuser:
#             # Redirect to admin panel if the user tries to access unauthorized pages
#             if request.path.startswith(settings.ADMIN_URL_PREFIX):
#                 logout(request)  # Logout non-admin users for security
#                 messages.error(request, 'Unauthorized access. Please log in as admin.')
#                 return render(request,'login.html')  # Replace with your login URL
        
#         return response
