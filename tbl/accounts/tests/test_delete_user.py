from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import User


class DeleteUserTestCase(APITestCase):
    """
    Unit test responsible for the removal of system users.
    """

    def setUp(self):
        """
        This method will run before any test.
        """

        self.superuser = User.objects.create_superuser(
            name='Victor Arnaud',
            email='victorhad@gmail.com',
            password='victorhad123456'
        )
        self.user = User.objects.create(
            name='Pedro Calile',
            email='pedro@gmail.com',
            password='pedro123456'
        )
        self.client.force_authenticate(self.user)

    def tearDown(self):
        """
        This method will run after any test.
        """

        self.superuser.delete()
        self.client.logout()
        self.user.delete()

    def test_valid_delete_user(self):
        """
        Delete your own user in the system.
        """

        url = reverse('accounts:details', kwargs={'pk': self.user.pk})
        self.assertEquals(User.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(User.objects.count(), 1)

    def test_invalid_delete_another_user(self):
        """
        Can't Delete another user of system.
        """

        url = reverse('accounts:details', kwargs={'pk': self.superuser.pk})
        self.assertEquals(User.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(User.objects.count(), 2)

    def test_not_find_user_to_delete(self):
        """
        Can't find user to delete, invalid url.
        """

        url_invalid = reverse('accounts:details', kwargs={'pk': 30})
        self.assertEquals(User.objects.count(), 2)
        response = self.client.delete(url_invalid)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(User.objects.count(), 2)
