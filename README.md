# ai_django

created home app -> settings.py add to installed apps
                -> urls.py created

ai_django -> urls.py linked to home.urls
        -> home.urls linked to home.views

created model in models.py -> added model to home/admin.py
                            -> makemigrations
                            -> migrate
                            -> accesses model in home.views

created index.html in templates folder -> settings.py template variable

created index.css in static -> STATICFILES_DIRS added

passed data to html in views -> accessed in html using variable

used shell inside terminal to interact with DB