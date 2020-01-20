# Building APIs using Python and Flask

### Advice: type all of the examples yourself and try to understand what's going on. Ask if in doubt!


In this workshop we will build a RESTfull API which
 - returns a list of most popular names

 - returns meaning for a specific name

 - adds a name to the list

 - deletes a name from the list

----------------
We are using Python3 and Flask framework to build the API.

------------------------
## Setup

1. Clone or download the github repository into your home dir:

    ``git clone https://github.com/elenaoat/codingmeetup.git``
2. Open the repository with your editor (PyCharm, Sublime, Atom, etc.)

3. Create a virtual environment.

    To isolate your global environment from the packages that we are about to install, we will create a virtual environment.
    So that you can install same packages but of different version later. It's best practice to always create a virtual
    environment for every project in Python.

    ``python3 -m venv venv``
4. Install the libraries.

    To install all the required dependencies (requests library, Flask) run:

    ``pip install -r requirements.txt``
