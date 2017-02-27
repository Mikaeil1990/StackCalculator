import unittest
import app




class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        print "==> Setting up the test environments."
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        self.app.get('/calc/1/push/1', content_type='html/text')
        self.app.get('/calc/1/push/2', content_type='html/text')
    def tearDown(self):
        print "==> Tear down the test environments."
        app.StacksHolder = {}

    def test_push(self):
        response = self.app.get('/calc/1/push/3', content_type='html/text')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, '3 Added!')

    def test_peek(self):
        response = self.app.get('/calc/1/peek', content_type='html/text')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data, '2')

    def test_pop(self):
        response = self.app.get('/calc/1/pop', content_type='html/text')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, '2')

    def test_add(self):
        response = self.app.get('/calc/1/add', content_type='html/text')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, '3')
    def test_sub(self):
        response = self.app.get('/calc/1/subtract', content_type='html/text')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, '-1')
    def test_mul(self):
        response = self.app.get('/calc/1/multiply', content_type='html/text')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, '2')
    def test_div(self):
        response = self.app.get('/calc/1/divide', content_type='html/text')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.data, '0')

if __name__ == '__main__':
    unittest.main()