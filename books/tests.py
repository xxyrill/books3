from django.contrib.auth import get_user_model # imports Reviews model
from django.contrib.auth.models import Permission
from django.test import Client, TestCase
from django.urls import reverse
# Client is used for testing views, creates a dummy web browser to simulate GET and POST requests on URL

from .models import Book, Review


class BookTests(TestCase):

    # the sample review test for user who will do the review
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )
        self.special_permission = Permission.objects.get(codename='special_status')
        # new

    # the sample book test
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00'
        )
    # the sample review test for the book and author that will be reviewed
        self.review = Review.objects.create (#
        book = self.book,
        author = self.user,
        review = 'An excellent review',
        )


    # passes values on book tests to check string representation and content are correct
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view_for_logged_in_user(self): # new
        self.client.login(email='reviewuser@email.com', password='testpass123')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_view_for_logged_out_user(self): # new
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '%s?next=/books/' % (reverse('account_login')))
        response = self.client.get(
            '%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

    def test_book_detail_view_with_permission(self): # new
        self.client.login(email='reviewuser@email.com', password='testpass123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'An excellent review')
        self.assertTemplateUsed(response, 'books/book_detail.html')

# old tests below, being replaced with other tests because new codes were added to the system
# you can use the tests code as reference for testing future system

    # test to confirm homepage returns 200 htttp code that contains the text body
#    def test_book_list_view(self):
        #        response = self.client.get(reverse('book_list'))
        #        self.assertEqual(response.status_code, 200)
        #       self.assertContains(response, 'Harry Potter')
    #       self.assertTemplateUsed(response, 'books/book_list.html')

    # test to confirm the detail page work and returns 404 for an incorrect page
    # this test will test something that exists and doesn't exist
        #   def test_book_detail_view(self):
        #       response = self.client.get(self.book.get_absolute_url())
        #      no_response = self.client.get('/books/12345/')
        #      self.assertEqual(response.status_code, 200)
        #      self.assertEqual(no_response.status_code, 404)
        #      self.assertContains(response, 'Harry Potter')
        #      self.assertContains(response, 'An excellent review')
#      self.assertTemplateUsed(response, 'books/book_detail.html')