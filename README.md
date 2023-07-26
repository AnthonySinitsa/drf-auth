# not clouds

- dcu -d

- http POST 0.0.0.0:8000/api/token/ username=admin password=admin

copy the access string

- http :8000/api/v1/not_clouds/ "Authorization: Bearer tokenjustcopied"

Do or don't use command idk, i think it works :/

- gunicorn not_clouds_project.wsgi

I don't get an error when ran so i think it's 'ready'
