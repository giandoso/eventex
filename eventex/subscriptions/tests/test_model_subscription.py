from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModuleTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Henrique Bastos',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='21-996186180',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """
        subscription must have an auto created_at attr
        """
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Henrique Bastos', str(self.obj))

    def test_paid_detault_to_False(self):
        self.assertEqual(False, self.obj.paid)