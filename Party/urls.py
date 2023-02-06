from django.urls import path
from . import views
from . import consumers



urlpatterns =[
    path('',views.showParty,name="party"),
    path('create/',views.crateParty,name='createparty'),
    path('<int:id>',views.partyDetail,name='partydetails'),
    path('<int:party_id>/update/',views.update_party,name='update'),
    path('<int:party_id>/join/', views.join, name='joins'),
    path('<int:party_id>/leave/', views.leave, name='leave'),
    path('<int:party_id>/delete/',views.delete_party,name="delete"),
    path("<int:party_id>/accept/<int:user_id>/", views.accept_member, name="accept_member"),
    path("<int:party_id>/reject/<int:user_id>/", views.reject_member, name="reject_member"),
    path("search_party/",views.search,name='search_party'),
    path('<int:party_id>/add_member/', views.add_member, name='add_member'),
    path('<int:party_id>/delete_member/<int:member_id>/', views.delete_member, name='delete_member'),
    path('<int:party_id>/like/', views.like_party, name='like_party'),
    path('<int:party_id>/unlike/', views.unlike_party, name='unlike_party'),
    path('<int:party_id>/dislike/', views.dislike_party, name='dislike_party'),
    path('<int:party_id>/undislike/', views.undislike_party, name='undislike_party'),
    path('<int:party_id>/upload_evidence/', views.upload_evidence, name='upload_evidence'),
    path('<int:party_id>/evidence/', views.show_evidence, name='show_evidence'),
    #path('<int:party_id>/delete_evidence/', views.delete_evidence, name='delete_evidence'),
    #path('ws/party/<int:party_id>/', consumers.ChatConsumer.as_asgi())
    
]
