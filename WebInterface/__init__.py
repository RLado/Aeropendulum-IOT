#__init__.py
#Flask app for the Aeropendulum_IOT project
#8th August 2019
#Ricard Lado <ricardlador@iqs.edu>


from flask import Flask

def create_app():
    app=Flask(__name__)

    from .views import main
    app.register_blueprint(main)

    return app
