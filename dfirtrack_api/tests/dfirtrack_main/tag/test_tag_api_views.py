from dfirtrack_main.models import Tag, Tagcolor
from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class TagAPIViewTestCase(TestCase):
    """ tag API view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_api_1')
        # create object
        tagcolor_2 = Tagcolor.objects.create(tagcolor_name='tagcolor_api_2')
        # create object
        Tag.objects.create(
            tag_name = 'tag_api_1',
            tagcolor = tagcolor_1,
        )
        # create user
        test_user = User.objects.create_user(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')

    def test_tag_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/tags/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_tag_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
        # get response
        response = self.client.get('/api/tags/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tag_list_api_method_post(self):
        """ POST is allowed """

        # get object
        tagcolor_id = str(Tagcolor.objects.get(tagcolor_name='tagcolor_api_2').tagcolor_id)
        # login testuser
        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
        # create POST string
        poststring = {
            "tag_name": "tag_api_2",
            "tagcolor": tagcolor_id,
        }
        # get response
        response = self.client.post('/api/tags/', data=poststring)
        # compare
        self.assertEqual(response.status_code, 201)

    def test_tag_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
        # create url
        destination = urllib.parse.quote('/api/tags/', safe='/')
        # get response
        response = self.client.get('/api/tags', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_tag_list_api_get_user_context(self):
#        """ test user context """
#
#        # login testuser
#        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
#        # get response
#        response = self.client.get('/api/tags/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_tag_api')

    def test_tag_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        tag_api_1 = Tag.objects.get(tag_name='tag_api_1')
        # get response
        response = self.client.get('/api/tags/' + str(tag_api_1.tag_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_tag_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        tag_api_1 = Tag.objects.get(tag_name='tag_api_1')
        # login testuser
        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
        # get response
        response = self.client.get('/api/tags/' + str(tag_api_1.tag_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tag_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        tag_api_1 = Tag.objects.get(tag_name='tag_api_1')
        # login testuser
        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
        # get response
        response = self.client.delete('/api/tags/' + str(tag_api_1.tag_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_tag_detail_api_method_put(self):
        """ PUT is allowed """

        # get object
        tagcolor_id = str(Tagcolor.objects.get(tagcolor_name='tagcolor_api_1').tagcolor_id)
        # get object
        tag_api_1 = Tag.objects.get(tag_name='tag_api_1')
        # login testuser
        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
        # create url
        destination = urllib.parse.quote('/api/tags/' + str(tag_api_1.tag_id) + '/', safe='/')
        # create PUT string
        putstring = {
            "tag_name": "new_tag_api_1",
            "tagcolor": tagcolor_id,
        }
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_tag_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        tag_api_1 = Tag.objects.get(tag_name='tag_api_1')
        # login testuser
        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
        # create url
        destination = urllib.parse.quote('/api/tags/' + str(tag_api_1.tag_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/tags/' + str(tag_api_1.tag_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

#    def test_tag_detail_api_get_user_context(self):
#        """ test user context """
#
#        # get object
#        tag_api_1 = Tag.objects.get(tag_name='tag_api_1')
#        # login testuser
#        login = self.client.login(username='testuser_tag_api', password='2SxcYh8yo3rGs4PBqhg9')
#        # get response
#        response = self.client.get('/api/tags/' + str(tag_api_1.tag_id) + '/')
#        # compare
#        self.assertEqual(str(response.context['user']), 'testuser_tag_api')
