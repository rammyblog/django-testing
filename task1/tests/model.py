from django.test import TestCase
from task1.models import Post
from django.contrib.auth.models import User
from model_bakery import baker
from pprint import pprint


class TestAppModels(TestCase):    
    @classmethod
    def setUpTestData(cls):
        print('db creation')
        testuser = User.objects.create_user(username='testuser', password='12345')
        testuser2 = User.objects.create_user(username='testuser2', password='12345')
        cls.new = Post.objects.create(title='Django Testing', content='content', slug='django')
        cls.new.likes.set([testuser.pk, testuser2.pk])
        
    
    def test_model_str(self):
        self.assertEqual(str(self.new), 'Django Testing')
        
    def test_post_like_users(self):
        # testuser = User.objects.create_user(username='testuser', password='12345')
        # testuser2 = User.objects.create_user(username='testuser2', password='12345')
        # title = Post.objects.create(title='Django Testing', content='content')
        # title.likes.set([testuser.pk, testuser2.pk])
        self.assertEqual(self.new.likes.count(), 2)
    
    def test_get_absolute_url(self):
        self.new.slug = Post.objects.get(id=1)
        self.assertEqual('/django/', self.new.slug.get_absolute_url())
    
    

class TestNew(TestCase):
    def setUp(self):
        self.post = baker.make('task1.Post')
        pprint(self.post.__dict__)
    
    
    def test_model_str(self):
        title = Post.objects.create(title="Django Testing")
        content = Post.objects.create(content="This is some content")
        self.assertEqual(str(title), "Django Testing")