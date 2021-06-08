#### Started Project for creating User management for the project where Producs are managing like Shopping web
```
step 1: django-admin startproject docskiff && cd docskiff
step 2: python manage.py startapp eshopping

```

Templates which i have used here for index.html is taken from. Its free so i have used to for displaying part
- https://themehunt.com/item/1524993-eshopper-best-free-ecommerce-html-template

After creating the project and app we have to make changes in urls.py to call the function from view.py
```
urlpatterns = [
    path('',views.index, name='index')
]

...

# In views.py we have to add the index()

def index(request):
    data = from orm we can collect the data
    return render(request, 'index.html', {'dataany':data})
```

setup the directories for templates and static files in Settings.py

```
  STATICDIRS = [os.path.join(BASE_DIR, 'eshopper')]
  STATIC
```

- Added media file to keep the record of images 

- added User Registration Login, Logout in the Useraccount app.
- Connected with Postgres db and storing the data into it. 
- Created one table using ORM (Products)

To run the application:
```
pip install requirement.txt
python manage.py runserver
```

Check the Db available in Postgres with name eshopping
if not then create the DB 

now run 
```
python manage.py migrate

```
above command will create the table in db so that we can proceed with the application
