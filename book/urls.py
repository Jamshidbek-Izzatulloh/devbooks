from django.urls import path
from .views import (LCBookView, RUDBookView, LCBookCategoryView, 
                    RUDBookCategoryView, LCAuthorView, RUDAuthorView)

urlpatterns = [
    #BookCategory API
    path('category/', LCBookCategoryView.as_view()),
    path('category/<pk>/', RUDBookCategoryView.as_view()),
    
    #Book API
    path('', LCBookView.as_view()),
    path('<pk>/', RUDBookView.as_view()),

    #Author API
    path('author/', LCAuthorView.as_view()),
    path('author/<pk>/', RUDAuthorView.as_view()),
]