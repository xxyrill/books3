from django.test import Client, TestCase
from django.urls import reverse
# Client is used for testing views, creates a dummy web browser to simulate GET and POST requests on URL

from .models import Book


class BookTests(TestCase):

    # the sample book test
    def setUp(self):
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00'
        )
    # passes values on book tests to check string representation and content are correct
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    # test to confirm homepage returns 200 htttp code that contains the text body
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    # test to confirm the detail page work and returns 404 for an incorrect page
    # this test will test something that exists and doesn't exist
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_detail.html')