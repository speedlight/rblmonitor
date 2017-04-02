from django.test import TestCase
from .models import Rbllist

class RblListTest(TestCase):

    def setUp(self):
        self.obj01 = Rbllist(name='Test RBL 01', url='test1.abuse.org')
        self.obj02 = Rbllist(name='Test RBL 02', url='test2.abuse.org')

    def test_ip_input(self):
        # "Test if the input is a valid ipv4 address"

    def test_doamin_input(self):
        # "Test if the input is a valid domain name"
