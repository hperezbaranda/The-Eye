from ast import arg
import logging
from .models import Log
from django.utils import timezone
from django.http import HttpResponse

def log_any_event(view_name):
    """
    Logs all the events occuring in a Django view, to the
    Log model.
    """
 
    def real_decorator(actual_view):
        """
        This is the actual decorator.
        """
 
        def wrapped_view(object,*args, **kwargs):
            print(args[0])
            try:
                #Run the view code
                response = actual_view(object,args[0])
                #If a response is generated without any Exception
                #coming up, logged the event and return it

                debug_entry = Log(
                    timestamp=timezone.now(),
                    view=view_name,
                    exceptionclass='',
                    level=logging.INFO,
                    message='Event created')
                debug_entry.save()
                return response
            except Exception as e:
                #If an unexpected Exception occurs, make a debug entry
                #and save it
                debug_entry = Log(
                    timestamp=timezone.now(),
                    view=view_name,
                    exceptionclass=str(e.__class__),
                    level=logging.ERROR,
                    message=str(e))
                debug_entry.save()
                #Return the Server Error(500) status code
                return HttpResponse(status=500)
 
        return wrapped_view
 
    return real_decorator