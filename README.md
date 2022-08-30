# Impact

The goal of this project is to improve, at maximum as possible, the overall performance and evaluate the ecodesign 
of any website.

## Installation
Copy the ``.env.example`` file and rename it ``.env``.
You **must** fill the ``SECRET_KEY``, `DATABASE_URL` otherwise the application will not properly work.

> Fill the ``SECRET_KEY`` with a long, random string.

Then, in order to be able to run the app, you must install its dependencies which are
listed in the ``requirements.txt`` file with pip:
````shell
$ pip install -r requirements.txt
````

Finally, you need to create the database which you specify in the ``.env`` file and migrate the tables:
````shell
$ python manage.py migrate
````

### Virtual Environments
Sometimes you want to keep libraries from polluting system installs 
or use a different version of libraries than the ones installed on the system.  
For this purpose, the standard library as of Python 3.3 comes with the "venv" 
module in order to help maintain these separate versions.
These are others libraries which do the same but here we'll keep with the standard.

For a more in-depth tutorial, 
check the [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html) documentation.

So, lets create our virtual environment:
1. Go to the ``purbeurre`` project directory:
    ```shell
    $ cd path/to/purbeurre
    ```
2. Create your virtual environment:
    ```shell
    $ python3 -m venv my_venv
    ```
3. Activate your virtual environment:
    ```shell
    $ source my_venv/bin/activate
    ```
    On Windows it will be a little different:
    ```shell
    $ my_venv\Scripts\activate.bat
    ```
   > If you use Powershell, the file to use is ``activate.ps1`` instead.

You now have finished setting up your virtual environment.

> To exit the virtual environment, simply type the command ``deactivate`` in your terminal

## Run on localhost
After the installation step, you can run the application through the `manage.py` but first you must build the css in 
order to have the styles applied:
````shell
$ python manage.py tailwind install && python manage.py tailwind build
````
Then you can start the development server by running the following command:
````shell
$ python manage.py runserver
````
> The ``runserver`` command is only for development purpose


### Building psycopg2 sources
[Link to the documentation](https://www.psycopg.org/docs/install.html#install-from-source)