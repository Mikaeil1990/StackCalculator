# StackCalculator

This is a repository for a RESTful API backend using Flask framework.
The app is already hosted on Heroku web server and can be accessed:

* https://stack-calculator.herokuapp.com/


## End-points:
* **/calc/:id/peek** :  returns stack[top]
* **/calc/:id/push/<n>** : pushes a number onto the stack
* **/calc/:id/pop** :  returns the top from the stack and removes it
* **/calc/:id/add** : removes the top and top-1 from the stack and replaces it with stack[top-1]+stack[top]
* **/calc/:id/subtract** : removes the top and top-1 from the stack and replaces it with stack[top-1]-stack[top]
* **/calc/:id/multiply** : removes the top and top-1 from the stack and replaces it with stack[top-1]*stack[top]
* **/calc/:id/divide** : removes the top and top-1 from the stack and replaces it with stack[top-1]/stack[top]

## How to use:

Install Python interpreter:
    #installing python
Installing the app dependencies:

    # command line in Mac and Linux
    $ pip install -r requirements.txt

### For running the server go to app directory:

    # command line in Mac and Linux
    $ python app.py

now app should be running. as your see the app is running on your local machine public ip and is accessible in the same network.

 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 290-671-582

### For running tests go to test package:

    # unittest
    python test_unittest.py
    # integration test
    python test_integ.py


The app directories:


Files | Des
------------ | -------------
Model | This is a python package holding Stack class which holds all the Stack characteristics.
test | This is a python package holding unittests and integration tests.
app.py | Server with endpoints.
app.cfg | Configure file for the app.
requirements.txt | app dependencies.
Procfile and runtime.txt | these files are requirements to deploy the app on heroku web-service.



Enjoy and have Fun,
Mikaeil