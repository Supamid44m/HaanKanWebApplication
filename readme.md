#
dont forget docker-compose up -d  before python manage.py migrate

#
export model graph

python manage.py graph_models -a -o name.png


(1146, "Table 'Haankan-webapp.socialaccount_socialapp_sites' doesn't exist")

showmigrations