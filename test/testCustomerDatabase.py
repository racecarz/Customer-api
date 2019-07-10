import sys
sys.path.append('../')

from unittest import TestCase
from database.model import Customer


class testCustomerDatabase(TestCase):

    def testNewCustomer(self):
        zach = Customer('zach', 'carson', 'carson.zachary@heb.com', '777 john doe', 'San Antoino', 'TX', '77777')
        self.assertEqual(Cusrtomer.last_name, 'carson')
