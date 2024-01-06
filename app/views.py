from typing import Any
from django.http import HttpRequest
from django.shortcuts import render
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from dataclasses import dataclass
import time

@dataclass
class User:
    name: str
    age: int
    sex: str
    
    def __str__(self) -> str:
        return self.name    

users = [
    User('james.jones', 28, 'Male'),
    User('jane.jones', 31, 'Female'),
    User('jim.jones', 37, 'Male'),
    User('chris.james', 45, 'Male'),
    User('donovan.james', 34, 'Male'),
    User('jimmy.kuperts', 39, 'Male')
]

class TestFlightView(TemplateView):

    template_name='page1.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)  
        return ctx
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)


def list_users(request: HttpRequest):    
    paginator = Paginator(users, 5)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        items = paginator.page(paginator.num_pages)
    return render(request, 'includes/testflight/table.html', {'users': items})