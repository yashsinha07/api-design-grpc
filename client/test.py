import unittest
from unittest.mock import patch

import client.inventory_client
from inventory_client import InventoryClient


class GetBookTitlesTest(unittest.TestCase):

    # MockTest
    # This test will run regardless of the server being up or down.
    @patch('client.inventory_client.InventoryClient')
    def test(self, Client):
        client.inventory_client.InventoryClient('localhost:blahblah')
        assert Client is client.inventory_client.InventoryClient
        assert Client.getBookTitle(["1001", "1002"])

    # Unit tests
    # The tests written below will run only when the server is up and running.
    def test_normal_case(self):
        inventoryClient = InventoryClient(serverAddress='localhost:50051')
        self.assertEqual(inventoryClient.getBookTitle(["1001", "1002"]),
                         ['Harry Potter', 'Fault In Our Stars'],
                         "Incorrect response.")

    def test_negative_case(self):
        inventoryClient = InventoryClient(serverAddress='localhost:50051')
        self.assertEqual(inventoryClient.getBookTitle(["1003"]), [''], "ISBN not found!")
