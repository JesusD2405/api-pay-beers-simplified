from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
import json

from src.domain.models.stockModel import StockModel
from src.data.mockRepository.stock.stockMockSerializer import StockMockSerializer

class StockTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('stock-list')  
    
    # FIXME: Pendiente por mejorar...
    def test_list_items(self):
        current_date = '2024-09-10 12:00:00'
        beers = [
            {
                "name": "Corona",
                "price": 115,
                "quantity": 2
            },
            {
                "name": "Quilmes",
                "price": 120,
                "quantity": 0
            },
            {
                "name": "Club Colombia",
                "price": 110,
                "quantity": 3
            }
        ]
        stock = StockModel(last_updated=current_date, beers=beers)

        response = self.client.get(self.url, format='json')
        response_data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response_data, StockMockSerializer.mapTo(stock))