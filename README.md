# Building APIs using Python and Flask

### Advice: type all of the examples yourself and try to understand what's going on. Ask if in doubt!


In this workshop we will build a RESTfull API which
 - returns list of most popular female and male names (method: GET, endpoint: /names)

 - returns meaning for each name  (method: GET, endpoint: /names/michael)

 - adds a name to the list (method: POST, endpoint: /names, data about the name will be sent in the body of the message)

 - deletes a name from the list (method: DELETE, endpoint: /names/timothy)

----------------
We are using Python3 and Flask framework to build the API.

------------------------
## Setup
We will be using terminal on Mac/Linux computers or command prompt on Windows.
1. Clone or download the github repository into your home dir:

    ``$ git clone https://github.com/elenaoat/codingmeetup.git``
2. Open the repository with your editor (PyCharm, Sublime, Atom, etc.)

3. Optional: Create a virtual environment.

    To isolate your global environment from the packages that we are about to install, we will create a virtual environment.
    So that later you can install same packages but of different version. It's a best practice to create a virtual
    environment for any new Python project.

    Open your terminal or command prompt and navigate inside the folder where you downloaded/cloned the code.
    The folder must be called something like `codingmeetup` or `codingmeetup-master`.
    Then run:
    
    ``$ python3 -m venv venv``

    Activate the environment by running:

    ``source venv/bin/activate``

    You should see a `venv` word in your terminal before the path.
4. Install the libraries.

     To install all the required dependencies (requests library, Flask) run:

    ``$ pip install -r requirements.txt``

5. Tell terminal where does your Flask application reside by running:

   `$ export FLASK_APP=app.py`

   On Windows in your command prompt run:
   
   ``set FLASK_APP=app.py``

6. Make Flask server reload data automatically on code changes:

    `$ export FLASK_ENV=development`

6. Run Flask server:
    ``flask run``

7. Now head over to http://127.0.0.1:5000/names



# Resources

Python3 download:
https://www.python.org/downloads/

Installing pip on Mac, Linux, Windows:
https://techworm.net/programming/install-pip-python-mac-windows-linux/

Another resource on pip installation:
https://projects.raspberrypi.org/en/projects/using-pip-on-windows/4

Documentation on Flask:
https://flask.palletsprojects.com/en/1.1.x/

JSONPlaceholder - Fake Online REST API for Testing and Prototyping
https://jsonplaceholder.typicode.com/
