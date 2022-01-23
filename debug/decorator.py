from ast import arg
from asyncio.log import logger
from http.client import BAD_REQUEST
import logging

from rest_framework import status
from .models import Log
from django.utils import timezone
from django.http import HttpResponse, HttpResponseBadRequest
from eye.log import getLog

logger = getLog('views.py')

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
            try:
                #Run the view code
                response = actual_view(object,*args,**kwargs)
                #If a response is generated without any Exception
                #coming up, logged the event and return it

                if not status.is_success(response.status_code):
                    debug_entry = Log(
                        timestamp=timezone.now(),
                        view=view_name,
                        exceptionclass=str(HttpResponseBadRequest.__name__),
                        level=logging.getLevelName(logging.ERROR),
                        message=response.data)
                    debug_entry.save()
                else:
                        
                    debug_entry = Log(
                        timestamp=timezone.now(),
                        view=view_name,
                        exceptionclass='',
                        level=logging.getLevelName(logging.INFO),
                        message=': '.join(map(str,[response.data]))
                        )
                    debug_entry.save()

                logger.info(debug_entry.message)
        
                return response

            except Exception as e:
                #If an unexpected Exception occurs, make a debug entry
                #and save it
                debug_entry = Log(
                    timestamp=timezone.now(),
                    view=view_name,
                    exceptionclass=str(e.__class__),
                    level=logging.getLevelName(logging.ERROR),
                    message=str(e))
                debug_entry.save()
                logger.error(debug_entry.message)
                #Return the Server Error(500) status code
                return HttpResponse(status=500)
 
        return wrapped_view
 
    return real_decorator