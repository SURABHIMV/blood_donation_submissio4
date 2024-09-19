
from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
 
 
def admin_test_function(user):
    if user.user_type=='admin':
        return True
    return False
 
 
def patient_test_function(user):
    if user.user_type=='patient':
        return True
    return False
 
 
def admin_access_only():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")
          
            if request.user.is_authenticated:
                if not admin_test_function(request.user):
                    return redirect("login")
                
            return view(request, *args, **kwargs)
           
        return _wrapped_view
    return decorator
 
 
def patient_access_only():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("user_login")
            if request.user.is_authenticated:
                if not patient_test_function(request.user):
                    return redirect("user_login")
            return view(request, *args, **kwargs)
        return _wrapped_view
    return decorator
 
 
# def principal_access_only(message_to_deliver="Not allowed to \
#             access the principal's page , login as principal !"):
#     def decorator(view):
#         @wraps(view)
#         def _wrapped_view(request, *args, **kwargs):
#             if not principal_test_function(request.user):
#                 messages.error(request, message_to_deliver)
#                 return redirect("user_urls:login-user")
#             return view(request, *args, **kwargs)
#         return _wrapped_view
#     return decorator