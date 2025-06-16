from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        #desactivar solo en test
        app.config["WTF_CSRF_ENABLED"] = False
        return app
    
    #prueba que la app exista
    def test_app_exist_web(self):
        self.assertIsNotNone(current_app)
    
    #verifica que el parametro de la configuracion sea True
    def test_app_in_testing_mode(self):
        self.assertTrue(current_app.config["TESTING"])

    #verifica los redirects
    def test_index_redirects(self):
        response = self.client.get(url_for("index"))
        #siempre poner assrtEqual y response.location porque sino no jala
        self.assertEqual(response.location, url_for("show_information"))

    #testea el get
    def test_show_information_get(self):
        response = self.client.get(url_for("show_information"))
        #esto es para ver si en realidad esta retornando 200
        self.assert200(response)

    #testeamos el post
    def test_show_information_post(self):
        test_form_fake = {
            "username": "Sebastian",
            "password": "12345678"
        }
        response = self.client.post(url_for("show_information"), data = test_form_fake)
        #comprobar a que endpoint queremos que se redirija la respuesta
        self.assertEqual(response.location, url_for("index"))