# Flask Restful Boilerplate
> simple boilerplate for flask restful app with sqlachemy.
#### Migrations 
Run `python manage.py migrate` for migrating your database.
#### Resources 
Run `python manage.py resource <name>` for creating new resource folder. Resgister all urls of that resource in `urls.py` file in that resource folder. Create blueprint for all resources and register in `urls.py` in root folder of your project.

#### Schema 
Create schemas in `schema` folder and use `@marshal_with` and `@use_kwargs` for proper working of swagger. Goto http://localhost:5000/docs/ for swagger docs.
#### Others 
You can create utils in `common/utils.py` file and define constants in `common/const.py`.
Send response using Response class (`from common.response import Response`).
If you want to log errors in file use `app.logger.error<any_other_function>() in your code` and add this line `from flask import current_app as app` for app.
