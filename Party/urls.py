from django.urls import path
from . import views
from . import consumers



urlpatterns =[
    path('',views.showParty,name="party"),
    path('create/',views.crateParty,name='createparty'),
    path('<int:id>',views.partyDetail,name='partydetails'),
    path('<int:id>/update/',views.update_party,name='update'),
    path('<int:id>/join/', views.join, name='joins'),
    path('<int:id>/leave/', views.leave, name='leave'),
    path("<int:party_id>/accept/<int:user_id>/", views.accept_member, name="accept_member"),
    path("<int:party_id>/reject/<int:user_id>/", views.reject_member, name="reject_member"),
    path("search_party/",views.search,name='search_party')
    #path('ws/party/<int:party_id>/', consumers.ChatConsumer.as_asgi())
    
]
