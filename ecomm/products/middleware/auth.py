from django.shortcuts import render,redirect
def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        returnURL = request.META['PATH_INFO']
        if not request.session.get('customer_id'):
            return redirect(f'login?return_url={returnURL}')
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware