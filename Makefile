superuser:
	docker exec -it impugnaciones ./manage.py createsuperuser

shell:
	docker exec -it impugnaciones ./manage.py shell

makemigrations:
	docker exec -it impugnaciones ./manage.py makemigrations

migrate:
	docker exec -it impugnaciones ./manage.py migrate

initialfixture:
	docker exec -it impugnaciones ./manage.py loaddata initial

statics:
	docker exec -it impugnaciones ./manage.py collectstatic --noinput

makemessages:
	docker exec -it impugnaciones django-admin makemessages

compilemessages:
	docker exec -it impugnaciones django-admin compilemessages

loadmmv:
	docker exec -it impugnaciones ./manage.py cargarmmv
