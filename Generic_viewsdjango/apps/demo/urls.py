from django.urls import path
from apps.demo import views
urlpatterns=[
    path('',views.Getview.as_view(),name="list"),
    path('detail/<int:pk>',views.Detailview.as_view(),name="detail"),
    path('create/',views.Createview.as_view(),name="create"),
    path('form/',views.Formview.as_view(),name="form"),
    path('update/<int:pk>',views.Updateview.as_view(),name="update"),
    path('delete/<int:pk>',views.Deleteview.as_view(),name="delete")
]