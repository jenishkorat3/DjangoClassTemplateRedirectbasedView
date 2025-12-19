from django.shortcuts import render
from django.views.generic.base import RedirectView


class HomeRedirectView(RedirectView):
    # url = '/'
    # pattern_name = "house"
    url = 'https://google.com'


class SuccessRedirectView(RedirectView):
    pattern_name = "login"
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        kwargs['pk'] = 23
        return super().get_redirect_url(*args, **kwargs)
